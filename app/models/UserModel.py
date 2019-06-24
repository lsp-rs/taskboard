from app import db
from sqlalchemy import DateTime, Enum


class User(db.Model):

    __tablename__ = "user"
    _valueStatus = ('ativo','inativo','desativado')
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(160), nullable = False)
    birthday = db.Column(db.Date, nullable = False)
    email = db.Column(db.String(150), nullable = False)
    password = db.Column(db.String(255), nullable = True)
    status = db.Column(db.Enum(_valueStatus), nullable = False)
    created = db.Column(db.Date, nullable = False)
    modified = db.Column(db.Date, nullable = True)

    def __init__(self, name, birthday, email, password, status, created, modified):
        self.name = name
        self.birthday = birthday
        self.email = email
        self.password = password
        self.status = status
        self.created = created
        self.modified = modified
