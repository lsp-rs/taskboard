from app.models.ListModel import List
from datetime import datetime as dtt


class ListDao():
    
    _lst = List()
    def insertList():
        try:
            _lst.session.add()
            _lst.session.commit()
            return "Success!"
        except Exception as e:
            return e

    def updateList(self, data):
        try:
            list_update = _lst.query.filter_by(id = data['id'])
            list_update.title =  data['list_items']
            list_update.modified = dtt.utcnow()
            list_update.session.commit()
            return "Success!"
        except Exception as e:
            return e
    
    def selectList(self):
        try:
            list_result = _lst.query.all()
            return list_result
        except Exception as e:
            return e
