from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

# App initialization
app = Flask(__name__)

# Load configuration
app.config.from_object('config')

# Create the database object
db = SQLAlchemy(app)

# Register modules, making them available to the application
from app.auth.views import mod as auth_mod
app.register_blueprint(auth_mod)

# Create the actual database tables. Do after registering modules
db.create_all()
