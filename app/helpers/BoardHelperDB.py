from app.models.BoardModel import Board
from datetime import datetime as dtt


class BoardDao():
    _brd = Board()

    def insertBoard(self, data):
        try:
            _brd.session.add(data)
            _brd.session.commit()
            return "Success!"
        except Exception as e:
            return 

    def ordenation(self, neworder):
        try:
            board_update = _brd.query.filter_by(id = data['id'])
            board_update.order = neworder
        except Exception as e:
            return e

    def updateBoard(self, data):
        try:
            board_update = _brd.query.filter_by(id = data['id'])
            board_update.title =  data['title']
            board_update.modified = dtt.utcnow()
            board_update.session.commit()
            return "Success!"
        except Exception as e:
            return e
    
    def selectBoard(self):
        try:
            board_result = _brd.query.all()
            return board_result
        except Exception as e:
            return e
