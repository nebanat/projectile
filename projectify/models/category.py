from projectify.extensions import db
from lib.util_sqlalchemy import ModelMixin


class Category(db.Model, ModelMixin):
    def __init__(self, name, description, slug):
        self.name = name
        self.description = description
        self.slug = slug

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    description = db.Column(db.String(500))
    slug = db.Column(db.String(130), unique=True)
