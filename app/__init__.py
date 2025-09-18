from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy()
# PENTING: Hubungkan db dengan app
db.init_app(app)
from app.route.main_route import main_bp
app.register_blueprint(main_bp)