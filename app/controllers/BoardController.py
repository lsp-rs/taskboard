from flask import session, redirect, url_for
from app.helpers.BoardHelperDB import BoardDao
from datetime import datetime

class BoardController():

    _brd = BoardDao()
    def listBoards(self, data):
        try:
            if 'user' in session:
                if session['user']['id']:
                    key_boards =[
                        'title_board',
                        'title_card',
                        'desc_card',
                        'name_annex',
                        'items_list',
                    ]
                    results = self._brd.selectBoard(data)
                    boards = []
                    for board in results: boards.append(dict(zip(key_boards,board)))
        except Exception as e:
            print(f'ERROR IN CONTROLLER(signUp): {e}')
            return False
        return boards
