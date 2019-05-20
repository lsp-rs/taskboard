import os
# from redis import Redis
# from datetime import timedelta


SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = 'mysql://lucas:51423@localhost/taskboard'

# SESSION_TYPE = 'redis'
# SESSION_REDIS = Redis(host=os.environ.get('REDIS_HOST'), port=os.environ.get('REDIS_PORT'), db=0)
# PERMANENT_SESSION_LIFETIME = timedelta(hours=24)

DEBUG = True
