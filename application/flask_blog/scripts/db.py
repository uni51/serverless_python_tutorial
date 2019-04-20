from flask_script import Command
from flask_blog.models.entries import Entry

class InitDB(Command):
    "create database"

    def run(self):
        if not Entry.exists(): # テーブルが存在しているかどうかを判定する
            Entry.create_table(read_capacity_units=5, write_capacity_units=2)
