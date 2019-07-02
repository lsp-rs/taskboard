from app.models.BoardModel import Board
from datetime import datetime
from app import db


class Card(db.Model):

    __tablename__ = "card"
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(60), nullable = False)
    description = db.Column(db.String(255), nullable = False)
    order = db.Column(db.Integer, nullable = False)
    board_id = db.Column(db.Integer, db.ForeignKey('board.id'), nullable=False)
    created = db.Column(db.Date, nullable = False, default=datetime.utcnow)
    modified = db.Column(db.Date, nullable = True, default=datetime.utcnow)

    def __init__(self, title, description, order, board_id):
        self.title = title
        self.description = description
        self.order = order
        self.board_id = board_id
