from datetime import datetime
from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute, NumberAttribute, UTCDateTimeAttribute
from flask_blog.lib.utils import is_production
import os


class Entry(Model):
    class Meta:
        table_name = "serverless_blog_entries"
        region = 'ap-northeast-1'
        if is_production():
            aws_access_key_id = os.environ.get('SERVERLESS_AWS_ACCESS_KEY_ID')
            aws_secret_access_key = os.environ.get('SERVERLESS_AWS_SECRERT_KEY')
        else:
            aws_access_key_id = 'AWS_ACEESS_KEY_ID'
            aws_secret_access_key = 'AWS_SECRET_ACCESS_KEY'
            host = "http://localhost:8000"
    id = NumberAttribute(hash_key=True, null=False) # 数値
    title = UnicodeAttribute(null=True) # 文字列
    text = UnicodeAttribute(null=True) # 文字列
    created_at = UTCDateTimeAttribute(default=datetime.now) # UTCベースの Datetime