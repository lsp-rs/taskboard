# app.py
import os
# import redis
from flask import Flask, Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session

app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config')

db = SQLAlchemy(app)

sess = Session()
sess.init_app(app)


from app import auth
from app import taskboard
app.register_blueprint(auth.bp)
app.register_blueprint(taskboard.bp)
