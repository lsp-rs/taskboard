from app.models.CardModel import Card
from datetime import datetime
from app import db


class Annex(db.Model):

    __tablename__ = "annex"
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(60), nullable = False)
    annex = db.Column(db.LargeBinary, nullable = False)
    type_archive = db.Column(db.String(45), nullable = False)
    card_id = db.Column(db.Integer, db.ForeignKey('card.id'), nullable=False)
    created = db.Column(db.Date, nullable = False, default=datetime.utcnow)
    modified = db.Column(db.Date, nullable = True, default=datetime.utcnow)

    def __init__(self, name, annex, type_archive, created, modified):
        self.name = name
        self.annex = annex
        self.type_archive = type_archive
        self.created = created
        self.modified = modified
 