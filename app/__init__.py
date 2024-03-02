from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config
from flask_socketio import SocketIO
import threading

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
socketio = SocketIO(app, cors_allowed_origins="*")       

from app import models, routes
from app.sync_database import sync_database
from app.models import clear_data, init_types

with app.app_context():
    clear_data(db.session)
    init_types()
    socketio.run(app, debug=True, port=5000)
    sync_thread = threading.Thread(target=sync_database, daemon=True)
    sync_thread.start() 
 

