from projectify.extensions import db
from lib.util_sqlalchemy import ModelMixin
from werkzeug.security import generate_password_hash, check_password_hash


class User(ModelMixin, db.Model):

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, index=True)
    email = db.Column(db.String(255), unique=True, index=True, nullable=False,
                      server_default='')
    password = db.Column(db.String(128), nullable=False, server_default='')

    @classmethod
    def encrypt_password(cls, plaintext_password):
        if plaintext_password:
            return generate_password_hash(plaintext_password)

        return None

    @classmethod
    def get_by_username_and_email(cls, username, email):
        return cls.query.filter((cls.username == username) | (cls.email == email)).first()

    def check_password(self, password):
        return check_password_hash(self.password, password)

    @classmethod
    def get_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    @classmethod
    def get_by_email(cls, email):
        return cls.query.filter_by(email=email).first()

    @classmethod
    def get_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()
