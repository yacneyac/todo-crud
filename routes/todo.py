from sqlalchemy import func
from sqlalchemy.exc import IntegrityError
from flask import request
from flask_restful import Resource


import models

from init_app import db, parser, StatusHTTP


parser.add_argument('status', type=int)
parser.add_argument('description', type=str)

MSG_MAP = {
    404: 'Todo with id={} is missed'
}


class TodoListAPI(Resource):
    @staticmethod
    def get():
        """ Find all todos in DB """
        # models.Todo.query.scalars().all()
        todos = db.session.execute(db.select(models.Todo)).scalars().all()
        return [todo.serialize() for todo in todos]

    @staticmethod
    def post():
        """ Create a new to-do with the status "new" """
        new_status = models.Status.query.filter_by(name='new').first()

        todo = models.Todo(
            description=request.json['description'],
            status=new_status.id
        )
        db.session.add(todo)
        try:
            db.session.commit()
        except IntegrityError as err:
            return {'message': err.orig.args}, StatusHTTP.SERVER_ERROR

        return todo.serialize(), StatusHTTP.CREATED


class TodoAPI(Resource):

    @staticmethod
    def get(t_id):
        """ Find to-do by ID """
        todo = db.get_or_404(models.Todo, t_id, description=MSG_MAP[404].format(t_id))
        return todo.serialize()

    @staticmethod
    def put(t_id):
        """ Update a to-do by ID """
        data = parser.parse_args()
        todo = models.Todo.query.filter_by(id=t_id).first_or_404(description=MSG_MAP[404].format(t_id))

        if all(val is None for val in data.values()):
            return {'message': 'Nothing to update! '
                               'The values are missed or the name of the fields are invalid'}\
                , StatusHTTP.BAD_REQUEST

        if data['status'] is not None:
            todo.status = data['status']

        if data['description'] is not None:
            todo.description = data['description']

        try:
            db.session.commit()
        except IntegrityError as err:
            return {'message': err.orig.args}, StatusHTTP.SERVER_ERROR

        return todo.serialize()

    @staticmethod
    def delete(t_id):
        """ Delete a to-do by ID """
        todo = models.Todo.query.filter_by(id=t_id).first_or_404(description=MSG_MAP[404].format(t_id))
        todo.is_deleted = 1
        todo.deleted = func.now()
        try:
            db.session.commit()
        except IntegrityError as err:
            return {'message': err.orig.args}, StatusHTTP.SERVER_ERROR

        return '', StatusHTTP.NO_CONTENT
