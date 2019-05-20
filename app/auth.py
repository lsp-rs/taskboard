from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)


bp = Blueprint('auth', __name__)

@bp.route('/register', methods=('GET', 'POST'))
def register():

    return render_template('auth/register.html')


@bp.route('/', methods=('GET', 'POST'))
def login():

    return render_template('auth/login.html')