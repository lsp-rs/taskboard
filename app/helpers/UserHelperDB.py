from app.models.UserModel import User
from datetime import datetime as dtt


class UserDao():

    _usr = User(name, birthday, email, password, status, created, modified)
    def insertUser(self, data):
        try:
            new_user = _usr(
                data['name'],
                data['birthday'],
                data['email'],
                data['password'],
                data['status'],
                dtt.utcnow(),
                dtt.utcnow()
            )
            db.session.add(new_user)
            db.session.commit()
        except Exception as e:
            return e
        return True

    def updateUser(self, data):
        try:
            user_update = _usr.query.filter_by(id = data['id'])
            user_update.name =  data['name']
            user_update.birthday =  data['birthday']
            user_update.email =  data['email']
            user_update.name =  data['status']
            user_update.modified = dtt.utcnow()
            user_update.session.commit()
        except Exception as e:
            return e
        return True
    
    def updateUserPassword(self, data):
        try:
            update_password = _usr.query.filter_by(id = data['id'])
            update_password.password =  data['password']
            user_update.session.commit()
        except Exception as e:
            return e
        return True

    def singInUser(self, data):
        try:
            user_result = _usr.query.with_entities(
                _usr.name,
                _usr.birthday,
                _usr.status,
                _usr.created
            ).filter_by(
                email = data['email'],
                password = data['password']
            )
        except Exception as e:
            return e
        return user_result
