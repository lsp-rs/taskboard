from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)


bp = Blueprint('auth', __name__)

@bp.route('/register', methods=('GET', 'POST'))
def register():
    if 'login' in session:
        if session['login']:
            return redirect(url_for('taskboard.home'))
    try:
        from app.controllers.UserController import UserController
        _usrCrtl = UserController()

        if request.method == 'POST':
            data = {
                'name' : request.form['name'],
                'birthday' : request.form['birthday'],
                'email' : request.form['email'],
                'password' : request.form['senha'],
                'status' : 'ativo'
            }
            if _usrCrtl.signUp(data):
                session['login'] = True
                return redirect(url_for('taskboard.home'))
    except Exception as e:
        print(f'ERRPR: {e}')
    return render_template('auth/register.html')


@bp.route('/', methods=('GET', 'POST'))
def login():
    session['login'] = False
    try:
        from app.controllers.UserController import UserController as usrCrtl

        if request.method == 'POST':
            data = {
                'email' : request.form['email'],
                'password' : request.form['senha']
            }
            if usrCrtl.signIn(data):
                session['login'] = True
                return redirect(url_for('taskboard.home'))
            message = "Login ou senha incorretos!"
            return render_template('auth/login.html', message = message)
        return render_template('auth/login.html')
    except Exception as e:
        return render_template('auth/login.html', error = e)