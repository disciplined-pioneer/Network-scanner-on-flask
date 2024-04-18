import sqlalchemy as sa
import sqlalchemy.orm as so
from app import app, db
import enum

def clear_data(session):
    meta = db.metadata
    for table in reversed(meta.sorted_tables):
        print('Clear table %s' % table)
        session.execute(table.delete())
    session.commit()
    
def init_types():
    db.session.add(InterfaceTypes(name="ETH"))
    db.session.add(InterfaceTypes(name="WLAN"))
    db.session.add(InterfaceTypes(name="VPN"))
    db.session.commit()

class InterfaceTypes(db.Model):
    __tablename__ = 'interface_types'
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    name: so.Mapped[str] = so.mapped_column(sa.String(50), unique=True, nullable=False)
    
    interfaces: so.Mapped["Interfaces"] = so.relationship('Interfaces', back_populates='type')
    
    def __repr__(self):
        return f"<InterfaceTypes(id={self.id}, name='{self.name}')>"
    
class InterfaceTypesEnum(enum.Enum):
    ETH = 1
    WLAN = 2
    VPN = 3

class Interfaces(db.Model):
    __tablename__ = 'interfaces'
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    ip: so.Mapped[str] = so.mapped_column(sa.String(15), unique=True, nullable=False)
    name: so.Mapped[str] = so.mapped_column(sa.String(50), unique=True, nullable=False)
    type_id: so.Mapped[int] = so.mapped_column(sa.Integer, sa.ForeignKey('interface_types.id'), nullable=False)
    description: so.Mapped[str] = so.mapped_column(sa.String(120))
    status: so.Mapped[str] = so.mapped_column(sa.String(10), nullable=False)
    
    type: so.Mapped["InterfaceTypes"] = so.relationship('InterfaceTypes', back_populates='interfaces')
    
    def __repr__(self):
        return f"<Interfaces(id={self.id}, name='{self.name}', type_id={self.type_id})>"
    
class SystemMetrics(db.Model):
    __tablename__ = 'system_metrics'
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    timestamp: so.Mapped[str] = so.mapped_column(sa.String(50), nullable=False)
    cpu_usage: so.Mapped[float] = so.mapped_column(sa.Float, nullable=False)
    memory_usage: so.Mapped[float] = so.mapped_column(sa.Float, nullable=False)
    network_sent: so.Mapped[float] = so.mapped_column(sa.Float, nullable=False)
    network_recv: so.Mapped[float] = so.mapped_column(sa.Float, nullable=False)

    def __repr__(self):
        return (f"<SystemMetrics(timestamp='{self.timestamp}', cpu_usage={self.cpu_usage}, "
                f"memory_usage={self.memory_usage}, network_sent={self.network_sent}, "
                f"network_recv={self.network_recv})>")

         