import functools
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from app.controllers.UserController import UserController
usr_ctrl = UserController()


bp = Blueprint('auth', __name__)

def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):        
        if not 'login' in session.keys():
            return redirect(url_for('auth.login'))
        return view(**kwargs)
    return wrapped_view

@bp.route('/', methods=('GET', 'POST'))
def login():
    try:
        if 'login' in session.keys():
            return redirect(url_for('taskboard.home'))
        if request.method == 'POST':
            data_login = {
                'email' : request.form['email'],
                'password' : request.form['password']
            }
            usr_ctrl.signIn(data_login)
            if session['login']:
                return redirect(url_for('taskboard.home'))
    except Exception as e:
        print(f'ERROR(login-view): {e}')

    return render_template('auth/login.html')

@bp.route('/logout')
def logout():
    usr_ctrl.singOut()
    return redirect(url_for('auth.login'))

@bp.route('/register', methods=('GET', 'POST'))
def register():
    if 'login' in session.keys():
        return redirect(url_for('taskboard.home'))
    try:
        if request.method == 'POST':
            data_register = {
                'name' : request.form['name'],
                'birthday' : request.form['birthday'],
                'email' : request.form['email'],
                'password' : request.form['password'],
                'status' : 'ativo'
            }
            if usr_ctrl.signUp(data_register):
                print(data_register)
                # return redirect(url_for('auth.login'))
    except Exception as e:
        print(f'ERROR(register-view): {e}')
    return render_template('auth/register.html')

