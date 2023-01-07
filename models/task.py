from sqlalchemy import func

from init_app import db


class Task(db.Model):
    __tablename__ = 'task'

    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(255))
    status = db.Column(db.Integer, db.ForeignKey('status.id'), nullable=False)
    created = db.Column(db.DateTime, server_default=func.now())

    def serialize(self):
        return {
            'id': self.id,
            'description': self.description,
            'status': self.status,
            'created': str(self.created)
        }
