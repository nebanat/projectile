from projectify.extensions import db


class ModelMixin(object):
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

        return self

    def delete_from_db(self):
        db.session.delete(self)
        return db.session.commit()
