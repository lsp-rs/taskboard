from app.models.CardModel import Card
from app import db


class List(db.Model):

    __tablename__ = "list"
    id = db.Column(db.Integer, primary_key = True)
    list_items = db.Column(db.Text(645), nullable = False)
    card_id = db.Column(db.Integer, db.ForeignKey('card.id'), nullable=False)

    def __init__(self, list_items, card_id):
        self.list_items = list_items
        self.card_id = card_id