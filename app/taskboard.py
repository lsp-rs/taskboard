from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)


bp = Blueprint('taskboard', __name__, url_prefix='/taskboard')

@bp.route('/home')
def home():
    if 'user' in session:
        if session['user']:
            from app.controllers.BoardController import BoardController
            _brd = BoardController()
            boards = _brd.listBoards(session['user']['id'])
            return render_template('taskboard/home.html', boards = boards)
    return redirect(url_for('auth.logout'))