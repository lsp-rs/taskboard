from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from app.controllers.BoardController import BoardController


_brd = BoardController()
bp = Blueprint('taskboard', __name__, url_prefix='/taskboard')
@bp.route('/home')
def home():
    if 'user' in session:
        boards = _brd.listBoards(session['user']['id'])
        return render_template('taskboard/home.html', boards = boards)
    return redirect(url_for('auth.logout'))

@bp.route('/board', methods = ['POST','GET'])
def addBoard():
    if request.method == 'POST':
        data = dict(request.form)
    if _brd.insertBoard(data):
        print("======================")
    return "Ok"