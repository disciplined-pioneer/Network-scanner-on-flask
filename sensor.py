import sqlalchemy as sa
import sqlalchemy.orm as so
from sqlalchemy import engine
from app import app, db, socketio
from app.models import InterfaceTypes, Interfaces, SystemMetrics

@app.shell_context_processor
def make_shell_context():
    return {'sa': sa, 'so': so, 'db': db, 'session': db.session, 'InterfaceTypes': InterfaceTypes, 'Interfaces': Interfaces, 'SystemMetrics': SystemMetrics, 'engine': engine}

    