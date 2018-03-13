from projectify.extensions import db
from lib.util_sqlalchemy import ModelMixin


class Project(db.Model, ModelMixin):
    def __init__(self, user_id, title, description, project_url, price, buyout_price):
        self.title = title
        self.description = description
        self.project_url = project_url
        self.price = price
        self.user_id = user_id
        self.buyout_price = buyout_price

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    description = db.Column(db.String(500))
    project_url = db.Column(db.String())
    price = db.Column(db.Integer)
    buyout_price = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship("User",
                           backref=db.backref("users", lazy="dynamic"))


