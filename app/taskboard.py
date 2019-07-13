from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from app.controllers.BoardController import BoardController
from app.controllers.CardController import CardController
from app.auth import login_required


_brd = BoardController()
_crd = CardController()
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
        message = "Board adicionado com sucesso!"
    return redirect(url_for('taskboard.home'))

@bp.route('/updateBoard', methods = ['POST','GET'])
@login_required
def updateBoard():
    if request.method == 'POST':
        data = dict(request.form)
    if _brd.updateBoard(data):
        message = "Alteração efetuada com sucesso!"
    return redirect(url_for('taskboard.home'))

@bp.route('/deleteBoard')
@bp.route('/deleteBoard/<int:id_board>/<int:confirmation>')
@login_required
def deleteBoard(id_board, confirmation):
    data = {
        'id_board' : id_board,
        'delete' : confirmation == 1
    }
    if _brd.deleteBoard(data):
        message = "Já pode dar tchau ao seu board!"
        print(message)
    return redirect(url_for('taskboard.home'))

@bp.route('/addCard', methods = ['POST','GET'])
@login_required
def addCard():
    if request.method == 'POST':
        data = dict(request.form)
    if _crd.insertCard(data):
        message = "Card adicionado com sucesso!"
    return redirect(url_for('taskboard.home'))

@bp.route('/updateCard', methods = ['POST','GET'])
@login_required
def updateCard():
    if request.method == 'POST':
        data = dict(request.form)
    if _crd.updateCard(data):
        message = "Card alterado com sucesso!"
    return redirect(url_for('taskboard.home'))

@bp.route('/deleteCard/<int:id_card>')
@login_required
def deleteCard(id_card):
    data = {
        'id': id_card,
        'confirma': 1
    }

    if _crd.deleteCard(data):
        message = "Card deletado com sucesso!"
    return redirect(url_for('taskboard.home'))
