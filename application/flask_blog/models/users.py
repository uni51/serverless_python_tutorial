from flask_login import UserMixin

class User(UserMixin): # UserMixinモデルを継承する
    def __init__(self, user_id):
        self.id = user_id

