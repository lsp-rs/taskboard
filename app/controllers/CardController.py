from flask import session, redirect, url_for
from app.helpers.CardHelperDB import CardDao
from datetime import datetime

class CardController():

    _crd = CardDao()
    def insertCard(self, data):
        try:
            if 'title_card' in data:
                self._crd.insertCard(data)
        except Exception as e:
            print(e)
            return False
        return True

    def deleteCard(self, data):
        try:
            if 'id' in data:
                self._crd.deleteCard(data)
        except Exception as e:
            print(e)
            return False
        return True

    def updateCard(self, data):
        try:
            if 'title_card' in data:
                self._crd.updateCard(data)
        except Exception as e:
            print(e)
        return True