import os

class DevelopmentConfig(object):
    DEBUG = True
    SECRET_KEY = 'secret key' # セッションを扱うためのシークレットキー
    USERNAME = 'john'
    PASSWORD = 'due123'

class ProductionConfig(object):
    DEBUG = False
    SECRET_KEY = os.environ.get('SERVERLESS_SECRET_KEY') # 指定した環境変数の値を読み込む
    USERNAME = 'john'
    PASSWORD = os.environ.get('SERVERLESS_USER_PW')