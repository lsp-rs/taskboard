from app.models.CardModel import Card
from datetime import datetime as dtt


class CardDao():

    _crd = CardCard()
    def insertCard(self, data):
        try:
            new_card = Card(
                data['title'],
                data['description'],
                1,
                data['board_id']
            )
            db.session.add(new_board)
            db.session.commit()
        except Exception as e:
            print(f'ERROR IN HELPER(insertCard): {e}')
            return False
        return True

    def updateCard(self, data):
        try:
            card_update = _crd.query.filter_by(id = data['id'])
            card_update.title =  data['title']
            card_update.title =  data['description']
            card_update.modified = dtt.utcnow()
            card_update.session.commit()
        except Exception as e:
            print(f'ERROR IN HELPER(updateCard): {e}')
            return False
        return True
