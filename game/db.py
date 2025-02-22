from peewee import SqliteDatabase, Model, CharField

db = SqliteDatabase('maslenica.db')


class User(Model):
    username = CharField(unique=True)
    score = CharField()

    class Meta:
        database = db


db.create_tables([User])
