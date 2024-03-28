import psutil
import time
from datetime import datetime
from app import app, db, socketio
from app.models import SystemMetrics, Interfaces, InterfaceTypesEnum

update_time = 1

def sync_metrics():
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cpu_usage = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory()
    memory_usage = memory.percent 
    net = psutil.net_io_counters()
    network_sent = net.bytes_sent / 1024 / 1024  # MB
    network_recv = net.bytes_recv / 1024 / 1024  # MB

    metric = SystemMetrics(
        timestamp=timestamp,
        cpu_usage=cpu_usage,
        memory_usage=memory_usage,
        network_sent=network_sent,
        network_recv=network_recv
    )

    with app.app_context():
        db.session.add(metric)
        db.session.commit()
        
    socketio.emit('update_metrics', {
        'timestamp': timestamp,
        'cpu_usage': cpu_usage,
        'memory_usage': memory_usage,
        'network_sent': network_sent,
        'network_recv': network_recv
    })

def get_network_interfaces():
    interfaces = []
    counter = 1
    for name, addrs in psutil.net_if_addrs().items():
        status = "Up" if psutil.net_if_stats().get(name, None).isup else "Down"
        
        type_id = 0
        if "ETH" in name.upper():
            type_id = InterfaceTypesEnum.ETH.value
        elif ("WIRELESS" or "WI-FI") in name.upper():
            type_id = InterfaceTypesEnum.WLAN.value
        else:
            type_id = InterfaceTypesEnum.VPN.value
        
        interface_info = {
            'id': counter,
            'ip': addrs[1][1],
            'name': name,
            'type_id': type_id, 
            'description': f"Interface {name}",
            'status': status
        }
        interfaces.append(interface_info)
        counter += 1
    
    return interfaces

from sqlalchemy.exc import OperationalError

def sync_interfaces():
    try:
        interfaces_info = get_network_interfaces()

        with app.app_context():
            for info in interfaces_info:
                interface = Interfaces.query.filter_by(name=info['name']).first()

                if interface:
                    interface.type_id = info['type_id']
                    interface.description = info['description']
                    interface.status = info['status']
                    interface.ip = info['ip']
                else:
                    interface = Interfaces(
                        name=info['name'],
                        ip=info['ip'],
                        type_id=info['type_id'],
                        description=info['description'],
                        status=info['status']
                    )
                    db.session.add(interface)
                    if interface.type:
                        info['type'] = interface.type.name
                    else:
                        type = ''
                        if info['type_id'] == InterfaceTypesEnum.ETH.value:
                            type = InterfaceTypesEnum.ETH.name
                        elif info['type_id'] == InterfaceTypesEnum.WLAN.value:
                            type = InterfaceTypesEnum.WLAN.name
                        elif info['type_id'] == InterfaceTypesEnum.VPN.value:
                            type = InterfaceTypesEnum.VPN.name
                        info['type'] = type

            db.session.commit()
            
            updated_interfaces_info = []
            interfaces = Interfaces.query.all()
            for interface in interfaces:
                updated_interfaces_info.append({
                    'id': interface.id,
                    'name': interface.name,
                    'ip': interface.ip,
                    'type_id': interface.type_id,
                    'description': interface.description,
                    'status': interface.status,
                    'type': interface.type.name if interface.type else 'Unknown'
                })

        socketio.emit('update_interfaces', updated_interfaces_info)
    except OperationalError as e:
        print(f"DB error: {e}")


def sync_database():
    while True:
        sync_interfaces()
        sync_metrics()
        time.sleep(update_time)   