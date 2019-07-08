from app.models.CardModel import Card, db
from datetime import datetime as dtt


class CardDao():

    def insertCard(self, data):
        try:
            new_card = Card(
                data['title_card'],
                data['desc_card'],
                1,
                data['id_board_card']
            )
            db.session.add(new_card)
            db.session.commit()
        except Exception as e:
            print(f'ERROR IN HELPER(insertCard): {e}')
            return False
        return True

    def updateCard(self, data):
        try:
            card_update = Card.query.filter(Card.id == data['id_card']).first()
            card_update.title =  data['title_card']
            card_update.description =  data['desc_card']
            card_update.modified = dtt.utcnow()
            db.session.commit()
        except Exception as e:
            print(f'ERROR IN HELPER(updateCard): {e}')
            return False
        return True
