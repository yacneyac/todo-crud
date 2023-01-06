from sqlalchemy import func
from datetime import datetime as dt

from init_app import db


class Todo(db.Model):
    __tablename__ = 'todo'

    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(255))
    status = db.Column(db.Integer, db.ForeignKey('status.id'), nullable=False)
    is_deleted = db.Column(db.Integer, default=0)  # 1 - deleted
    created = db.Column(db.DateTime, server_default=func.now())
    deleted = db.Column(db.DateTime)

    def serialize(self):
        return {
            'id': self.id,
            'description': self.description,
            'status': self.status,
            'is_deleted': self.is_deleted,
            'created': str(self.created),
            'deleted': str(self.deleted) if self.deleted else None
        }
