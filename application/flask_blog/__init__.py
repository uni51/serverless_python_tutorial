from flask import Flask
from flask_login import LoginManager
import os # 環境変数を読み込むため、標準のosライブラリをインポートする

# config情報の定義
config = {
    'default': 'flask_blog.config.DevelopmentConfig',
    'development': 'flask_blog.config.DevelopmentConfig',
    'production': 'flask_blog.config.ProductionConfig'
}

# Flaskアプリケーションの本体を作成する
app = Flask(__name__)

# configファイルを読み込む
config_name = os.getenv('SERVERLESS_BLOG_CONFIG', 'default')
app.config.from_object(config[config_name])

# login_managerを作成する（全ての箇所で、ログインマネージャーが有効になる）
login_manager = LoginManager()
login_manager.init_app(app)

# lib/utils.pyから、user_loaderを実装した関数を読み込む
from flask_blog.lib.utils import setup_auth
setup_auth(app, login_manager)

# 作成したビューファイルが参照できるように読み込む
from flask_blog.views import views, entries

# login_managerのオプション設定をする
from flask_blog.views.views import login
# ログインされていない場合は、login_view を指定することで指定のビューにリダイレクトするようにする。
login_manager.login_view = "login"
login_manager.login_message = "ログインしてください"
