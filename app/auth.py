from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)


bp = Blueprint('auth', __name__)

@bp.route('/register', methods=('GET', 'POST'))
def register():
    try:
        if request.method == 'POST':
            _user = request.form['email']
            _password = request.form['senha']
            if _user == 'lucas@teste.com' and _password == 'a1b2c3':
                _login = True

        if _login:
            return redirect(url_for('taskboard.home'))
    except:
        return render_template('auth/register.html')


@bp.route('/', methods=('GET', 'POST'))
def login():
    try:
        if request.method == 'POST':
            _user = request.form['email']
            _password = request.form['senha']
            if _user == 'lucas@teste.com' and _password == 'a1b2c3':
                _login = True

        if _login:
            return redirect(url_for('taskboard.home'))
    except:
        return render_template('auth/login.html')