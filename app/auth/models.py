from app import db
from passlib.apps import custom_app_context as pwd_context

# Some common model fields
class Base(db.Model):
    __abstract__  = True
    id            = db.Column(db.Integer, primary_key=True)
    date_created  = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
                              onupdate=db.func.current_timestamp())

# User Model
class User(Base):
    __tablename__ = 'auth_user'
    username      = db.Column(db.String(128), nullable=False)
    email         = db.Column(db.String(128), nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    def __init__(self, username=None, email=None, password=None):
        self.username      = username
        self.email         = email
        self.password_hash = self.create_password_hash(password)

    def create_password_hash(self, password):
        return pwd_context.encrypt(password)

    def verify_password(self, password):
        return pwd_context.verify(password, self.password_hash)

    @property
    def to_json(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
        }
