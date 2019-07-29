import datetime
from peewee import *
from flask.ext.login import UserMixin
from flask.ext.bcrypt import generate_password_hash

class User(UserMixin, Model):
    username = CharField(unique=True)
    email = CharField(unique=True)
    password = CharField(max_length=100)
    joined_at = DateTimeField(default=datetime.datetime.now)
    is_admin = BooleanField(default=False)
    bio = TextField(default='')


    class Meta:
        database = Database
        order_by = ('-joined_at',)


    @classmethod
    def create_user(cls, username, email, password, admin=False):
        try:
            cls.create(
                username = username,
                email = email,
                password = generate_password_hash(password),
                is_admin = admin
            )
        except IntegrityError:
            raise ValueError('already taken')
