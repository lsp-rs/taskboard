from app.models.AnnexModel import Annex
from datetime import datetime as dtt


class AnnexDao():

    _anx = Annex()

    def insertAnex(self, data):
        try:
            _anx.session.add(data)
            _anx.session.commit()
            return "Success!"
        except Exception as e:
            return 

    def updateAnnex(self, data):
        try:
            annex_update = _anx.query.filter_by(id = data['id'])
            annex_update.name =  data['name']
            annex_update.annex = data['annex']
            annex_update.type_archive = data['type_archive']
            annex_update.modified = dtt.utcnow()
            annex_update.session.commit()
            return "Success!"
        except Exception as e:
            return e
    
    def selectAnnex(self):
        try:
            annex_result = _anx.query.all()
            return annex_result
        except Exception as e:
            return e
