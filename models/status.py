from init_app import db


class Status(db.Model):
    __tablename__ = 'status'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False, unique=True)  # 'new', 'done', 'in_work'

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name
        }
