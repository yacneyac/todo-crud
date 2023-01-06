from flask_restful import Resource


from models.status import Status
from init_app import db


class StatusAPI(Resource):

    @staticmethod
    def get():
        statuses = db.session.execute(db.select(Status)).scalars().all()
        return [status.serialize() for status in statuses]

