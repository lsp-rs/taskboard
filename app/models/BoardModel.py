from app import db
from sqlalchemy import DateTime


class Board(db.Model):

    __tablename__ = "board"
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(60), nullable = False)
    order = db.Column(db.Integer, nullable = False)
    created = db.Column(db.Date, nullable = False)
    modified = db.Column(db.Date, nullable = True)

    def __init__(self, title, order, created, modified):
        self.title = title
        self.order = order
        self.created = created
        self.modified = modified
