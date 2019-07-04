from flask import session, redirect, url_for
from app.helpers.BoardHelperDB import BoardDao
from datetime import datetime

class BoardController():

    _brd = BoardDao()
    def listBoards(self, data):
        try:
            if 'user' in session:
                if session['user']['id']:
                    results = self._brd.selectBoard(data)
                    aux = 0
                    boards = []
                    list_board = []
                    for boards in results:
                        if boards[0] == aux:
                            cards.append({
                                'id_card': boards[2],
                                'title_card': boards[3],
                                'desc_card': boards[4],
                                'name_annex': boards[5],
                                'items_list': boards[6]
                            })
                        else:
                            cards = [{
                                'id_card': boards[2],
                                'title_card': boards[3],
                                'desc_card': boards[4],
                                'name_annex': boards[5],
                                'items_list': boards[6]
                            }]
                            list_board.append({
                                'id_board':boards[0],
                                'title_board':boards[1],
                                'cards': cards
                            })
                        aux = boards[0]
                    

        except Exception as e:
            print(f'ERROR IN CONTROLLER(signUp): {e}')
            return False
        return list_board
    
    def insertBoard(sef, data):
        try:
            print(data)
        except Exception as e:
            print(e)
            return False
        return True
