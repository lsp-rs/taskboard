from app import db


class List(db.Model):

    __tablename__ = "list"
    id = db.Column(db.Integer, primary_key = True)
    list_items = db.Column(db.String(645), nullable = False)

    def __init__(self, list_items):
        self.list_items = list_items
 