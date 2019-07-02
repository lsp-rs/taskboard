from flask import session, redirect, url_for
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
            print(f'count? {self._usr.singInUser(data)}')
            if self._usr.singInUser(data) == 1:
                usr_data = self._usr.userData(data)
                session['user'] = {
                    'id': usr_data[0].id,
                    'name': usr_data[0].name,
                    'birthday': usr_data[0].birthday,
                    'status': f'{usr_data[0].status.value}',
                    'created': usr_data[0].created,
                }
                session['login']= True
            else:
                session['login'] = False
        except Exception as e:
            print(f'ERROR IN CONTROLLER(signIn): {e}')
            return False
        return True

    def loginExist(self):
        if 'login' in session:
            if session['login']:
                return redirect(url_for('taskboard.home'))

    def singOut(self):
        if 'login' in session:
            if session['login']:
                session.clear()
                session['login'] = False