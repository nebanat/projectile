from projectify.extensions import db


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, index=True)
    email = db.Column(db.String(80), unique=True, index=True)
    password = db.Column(db.String(128), nullable=False)

