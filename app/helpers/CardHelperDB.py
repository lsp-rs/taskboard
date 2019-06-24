from app.models.CardModel import Card
from datetime import datetime as dtt


class CardDao():

    _crd = CardCard()

    def insertCard(self, data):
        try:
            _crd.session.add(data)
            _crd.session.commit()
            return "Success!"
        except Exception as e:
            return 

    def ordenation(self, neworder):
        try:
            card_update = _crd.query.filter_by(id = data['id'])
            card_update.order = neworder
        except Exception as e:
            return e

    def updateCard(self, data):
        try:
            card_update = _crd.query.filter_by(id = data['id'])
            card_update.title =  data['title']
            card_update.title =  data['description']
            card_update.modified = dtt.utcnow()
            card_update.session.commit()
            return "Success!"
        except Exception as e:
            return e
    
    def selectCard(self):
        try:
            card_result = _crd.query.all()
            return card_result
        except Exception as e:
            return e
