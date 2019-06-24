from app.helpers.UserHelperDB import UserDao


class UserController():

    _usr = UserDao()
    def signUp(self, data):
        try:
            _usr.insertUser(data)
        except Exception as e:
            return e
        return True

    def signIn(self, data):
        try:
            _usr.singInUser(data)
        except Exception as e:
            return e
        return True
