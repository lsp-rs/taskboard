from flask import session
from app.helpers.UserHelperDB import UserDao
from datetime import datetime


class UserController():

    _usr = UserDao()
    def signUp(self, data):
        try:
            self._usr.insertUser(data)
        except Exception as e:
            print(f'ERROR IN CONTROLLER(signUp): {e}')
            return False
        session['login'] = True
        
        session['user'] = {
            'name': data['name'],
            'email': data['email'],
            'birthday': data['birthday'],
            'status': data['status'],
            'created': datetime.utcnow(),
        }
        session['name'] = data['name']
        session['email'] = data['email']
        return True

    def signIn(self, data):
        try:
            if self._usr.singInUser(data) == 1:
                usr_data = self._usr.userData(data)
                session['user'] = {
                    'name': usr_data[0].name,
                    'birthday': f'{usr_data[0].birthday.day}/{usr_data[0].birthday.month}/{usr_data[0].birthday.year}',
                    'status': f'{usr_data[0].status.value}',
                    'created': usr_data[0].created,
                }
                session['login']= True
        except Exception as e:
            print(f'ERROR IN CONTROLLER(signIn): {e}')
            return False
        return True
