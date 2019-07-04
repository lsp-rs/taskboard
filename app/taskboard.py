from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from app.controllers.BoardController import BoardController
from app.auth import login_required


_brd = BoardController()
bp = Blueprint('taskboard', __name__, url_prefix='/taskboard')
@bp.route('/home')
@login_required
def home():
    if 'user' in session:
        boards = _brd.listBoards(session['user']['id'])
        return render_template('taskboard/home.html', boards = boards)
    return redirect(url_for('auth.logout'))

@bp.route('/addBoard', methods = ['POST','GET'])
@login_required
def addBoard():
    if request.method == 'POST':
        data = dict(request.form)
    if _brd.insertBoard(data):
        print("======================")
    return "Ok"


@bp.route('/updateBoard', methods = ['POST','GET'])
@login_required
def updateBoard():
    if request.method == 'POST':
        data = dict(request.form)
    if _brd.insertBoard(data):
        print("======================")
    return "Ok"

@bp.route('/addCard', methods = ['POST','GET'])
@login_required
def addCard():
    if request.method == 'POST':
        data = dict(request.form)
    if _brd.insertBoard(data):
        print("======================")
    return "Ok"

@bp.route('/updateCard', methods = ['POST','GET'])
@login_required
def updateCard():
    if request.method == 'POST':
        data = dict(request.form)
    if _brd.insertBoard(data):
        print("======================")
    return "Ok"