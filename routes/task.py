from sqlalchemy.exc import IntegrityError
from flask import request
from flask_restful import Resource, reqparse


import models

from init_app import db
from utils import StatusHTTP


parser = reqparse.RequestParser()
parser.add_argument('status', type=int)
parser.add_argument('description', type=str)

MSG_MAP = {
    404: 'Task with id={} is missed'
}


class TaskListAPI(Resource):
    @staticmethod
    def get():
        """ Find all tasks in DB """
        tasks = models.Task.query.all()
        return [task.serialize() for task in tasks]

    @staticmethod
    def post():
        """ Create a new to-do with the status "new" """
        new_status = models.Status.\
            query.\
            filter_by(name='new').\
            first()

        if not request.json.get('description'):
            return {'message': 'The "description" parameter is missed'}, StatusHTTP.BAD_REQUEST

        task = models.Task(
            description=request.json['description'],
            status=new_status.id
        )
        db.session.add(task)
        try:
            db.session.commit()
        except IntegrityError as err:
            print(err.orig.args)
            return {'message': 'server error'}, StatusHTTP.SERVER_ERROR

        return task.serialize(), StatusHTTP.CREATED


class TaskAPI(Resource):

    @staticmethod
    def get(t_id):
        """ Find task by ID """
        task = db.get_or_404(
            models.Task,
            t_id,
            description=MSG_MAP[404].format(t_id)
        )
        return task.serialize()

    @staticmethod
    def put(t_id):
        """ Update task by ID """
        data = parser.parse_args()
        task = models.Task.\
            query.\
            filter_by(id=t_id).\
            first_or_404(description=MSG_MAP[404].format(t_id))

        if all(val is None for val in data.values()):
            return {'message': 'Nothing to update! '
                               'The values are missed or the name of the fields are invalid'}\
                , StatusHTTP.BAD_REQUEST

        if data['status'] is not None:
            task.status = data['status']

        if data['description'] is not None:
            task.description = data['description']

        try:
            db.session.commit()
        except IntegrityError as err:
            print(err.orig.args)
            return {'message': 'server error'}, StatusHTTP.SERVER_ERROR

        return task.serialize()

    @staticmethod
    def delete(t_id):
        """ Delete task by ID """
        task = models.Task.\
            query.\
            filter_by(id=t_id).\
            first_or_404(description=MSG_MAP[404].format(t_id))

        db.session.delete(task)
        try:
            db.session.commit()
        except IntegrityError as err:
            print(err.orig.args)
            return {'message': 'server error'}, StatusHTTP.SERVER_ERROR

        return '', StatusHTTP.NO_CONTENT
