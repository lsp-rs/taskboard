from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)


bp = Blueprint('taskboard', __name__, url_prefix='/taskboard')

@bp.route('/home')
def home():

    return render_template('taskboard/home.html')