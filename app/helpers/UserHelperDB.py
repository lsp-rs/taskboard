from app.models.UserModel import User, db
from sqlalchemy import and_


class UserDao():

    def insertUser(self, data):
        try:
            new_user = User(
                data['name'],
                data['birthday'],
                data['email'],
                data['password'],
                data['status']
            )
            db.session.add(new_user)
            db.session.commit()
        except Exception as e:
            print(f'ERROR IN HELPER: {e}')
            return False
        return True

    def updateUser(self, data):
        try:
            user_update = self._usr.query.filter_by(id = data['id'])
            user_update.name =  data['name']
            user_update.birthday =  data['birthday']
            user_update.email =  data['email']
            user_update.name =  data['status']
            user_update.modified = dtt.utcnow()
            user_update.session.commit()
        except Exception as e:
            print(f'ERROR IN HELPER: {e}')
            return False
        return True
    
    def updateUserPassword(self, data):
        try:
            update_password = self._usr.query.filter_by(id = data['id'])
            update_password.password =  data['password']
            user_update.session.commit()
        except Exception as e:
            print(f'ERROR IN HELPER: {e}')
            return False
        return True

    def singInUser(self, data):
        try:
            user_result = User.query.filter(
                and_(
                    User.email == data['email'],
                    User.password == data['password']
                )
            ).count()
        except Exception as e:
            print(f'ERROR IN HELPER: {e}')
            return False
        return user_result

    def userData(self, data):
        try:
            user_result = User.query.with_entities(
                User.name,
                User.birthday,
                User.status,
                User.created
            ).filter(
                and_(
                    User.email == data['email'],
                    User.password == data['password']
                )
            ).all()
        except Exception as e:
            print(f'ERROR IN HELPER: {e}')
            return False
        return user_result
