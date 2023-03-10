from flask_restful import Resource


import models


class StatusAPI(Resource):

    @staticmethod
    def get():
        """ Get all statuses """
        statuses = models.Status.query.all()
        return [status.serialize() for status in statuses]
