from flask import Flask

from app.config import Config
from app.extensions import db, migrate, socketio
from app.routes.auth_routes import auth_bp
from app.routes.task_routes import task_bp
from app.routes.analytics_routes import analytics_bp

from app.models.user import User
from app.models.task import Task

def create_app():

    app = Flask(__name__)

    app.config.from_object(Config)

    db.init_app(app)

    migrate.init_app(app, db)

    socketio.init_app(app)

    app.register_blueprint(auth_bp)
    app.register_blueprint(task_bp)

    app.register_blueprint(analytics_bp)

    return app