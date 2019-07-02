from app.models.UserModel import User
from datetime import datetime
from app import db


class Board(db.Model):

    __tablename__ = "board"
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(60), nullable = False)
    order = db.Column(db.Integer, nullable = False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    created = db.Column(db.Date, nullable = False, default=datetime.utcnow)
    modified = db.Column(db.Date, nullable = True, default=datetime.utcnow)

    def __init__(self, title, order, user_id):
        self.title = title
        self.order = order
        self.user_id = user_id
