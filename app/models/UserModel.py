from app import db
from datetime import datetime
import enum


class Status(enum.Enum):
    ativo = 1
    inativo = 2
    desativado = 3

class User(db.Model):

    __tablename__ = "user"   
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(160), nullable = False)
    birthday = db.Column(db.Date, nullable = False)
    email = db.Column(db.String(150), nullable = False)
    password = db.Column(db.String(255), nullable = True)
    status = db.Column(db.Enum(Status), nullable = False)
    created = db.Column(db.Date, nullable = False, default=datetime.utcnow)
    modified = db.Column(db.Date, nullable = True, default=datetime.utcnow)

    def __init__(self, name, birthday, email, password, status):
        self.name = name
        self.birthday = birthday
        self.email = email
        self.password = password
        self.status = status