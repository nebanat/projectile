from datetime import datetime
from projectify.extensions import db


class ModelMixin(object):
    created_on = db.Column(db.DateTime, default=datetime.utcnow)
    updated_on = db.Column(db.DateTime,
                           default=datetime.utcnow, onupdate=datetime.utcnow)

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

        return self

    def delete_from_db(self):
        db.session.delete(self)
        return db.session.commit()

    @classmethod
    def filter_by(cls, **kwargs):
        return cls.query.filter_by(**kwargs).first()
