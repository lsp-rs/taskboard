from app.models.BoardModel import Board
from app.models.CardModel import Card
from app.models.AnnexModel import Annex
from app.models.ListModel import List
from datetime import datetime as dtt
from flask import session, redirect, render_template, url_for


class BoardDao():
    
    def insertBoard(self, data):
        try:
            new_board = Board(
                data['title'],
                1,
                session['user']['id']
            )
            db.session.add(new_board)
            db.session.commit()
        except Exception as e:
            print(f'ERROR IN HELPER(insertBoard): {e}')
            return False
        return True
    
    def selectBoard(self, data):
        try:

            board_result = Board.query.with_entities(
                Board.id,
                Board.title,
                Card.id,
                Card.title,
                Card.description,
                Annex.name,
                List.list_items
            ).outerjoin(
                Card, Card.board_id == Board.id
            ).outerjoin(
                Annex, Annex.card_id == Card.id
            ).outerjoin(
                List, List.card_id == Card.id
            ).filter(
                Board.user_id == data
            ).all()

        except Exception as e:
            print(f'ERROR IN HELPER(selectBoard): {e}')
            return False
        return board_result

    def updateBoard(self, data):
        try:
            board_update = _brd.query.filter_by(id = data['id'])
            board_update.title =  data['title']
            board_update.modified = dtt.utcnow()
            board_update.session.commit()
        except Exception as e:
            print(f'ERROR IN HELPER(updateBoard): {e}')
            return False
        return True
