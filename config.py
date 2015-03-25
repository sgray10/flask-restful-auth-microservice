# Enable Debugging in development
DEBUG = True

# Application directory
import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# Set the secret key
SECRET_KEY = 'the world is round'

# Databases
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'app.db')
SQLALCHEMY_COMMIT_ON_TEARDOWN = True
