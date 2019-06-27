from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from app.controllers.UserController import UserController
usr_ctrl = UserController()


bp = Blueprint('auth', __name__)

@bp.route('/register', methods=('GET', 'POST'))
def register():
    if 'login' in session:
        if session['login']:
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
                return redirect(url_for('taskboard.home'))
    except Exception as e:
        print(f'ERROR(register-view): {e}')
    return render_template('auth/register.html')


@bp.route('/', methods=('GET', 'POST'))
def login():
    try:
        if request.method == 'POST':
            data_login = {
                'email' : request.form['email'],
                'password' : request.form['password']
            }
            if usr_ctrl.signIn(data_login):
                return redirect(url_for('taskboard.home'))
    except Exception as e:
        print(f'ERROR(login-view): {e}')
    return render_template('auth/login.html')