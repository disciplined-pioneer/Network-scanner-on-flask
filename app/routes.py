from flask import render_template, redirect, url_for, request
from app import app, db
from app.models import Interfaces, SystemMetrics

def get_interfaces():
    return db.session.query(Interfaces).order_by(Interfaces.id.asc()).all()

@app.route('/')
@app.route('/index')
def index():
    interfaces = get_interfaces()
    return render_template('index.html', interfaces=interfaces)

@app.route('/metrics')
def metrics():
    metrics = db.session.query(SystemMetrics).order_by(SystemMetrics.timestamp.desc()).limit(10).all()
    return render_template('metrics.html', metrics=metrics)