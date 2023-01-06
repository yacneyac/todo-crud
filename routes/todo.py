# from datetime import datetime as dt
from sqlalchemy import func
from sqlalchemy.exc import IntegrityError
from flask import request
from flask_restful import Resource
# from werkzeug.http import HTTP_STATUS_CODES


import models

from init_app import db, parser


parser.add_argument('status', type=int, required=True, help='status is required')
parser.add_argument('description', type=str, required=False)

MSG_MAP = {
    404: 'Todo with id={} is missed'
}


class TodoListAPI(Resource):
    @staticmethod
    def get():
        """ Find all todos in DB """
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
            return {'message': err.orig.args}, 500

        return todo.serialize(), 201


class TodoAPI(Resource):

    @staticmethod
    def get(t_id):
        """ Find to-do by ID """
        todo = db.get_or_404(models.Todo, t_id, description=MSG_MAP[404].format(t_id))
        return todo.serialize()

    @staticmethod
    def put(t_id):
        """ Update a to-do by ID """
        args = parser.parse_args()
        todo = models.Todo.query.filter_by(id=t_id).first_or_404(description=MSG_MAP[404].format(t_id))
        todo.status = args['status']

        if args['description'] is not None:
            todo.description = args['description']

        try:
            db.session.commit()
        except IntegrityError as err:
            return {'message': err.orig.args}, 500

        return todo.serialize(), 200

    @staticmethod
    def delete(t_id):
        """ Delete a to-do by ID """
        todo = models.Todo.query.filter_by(id=t_id).first_or_404(description=MSG_MAP[404].format(t_id))
        todo.is_deleted = 1
        todo.deleted = func.now()
        try:
            db.session.commit()
        except IntegrityError as err:
            return {'message': err.orig.args}, 500

        return '', 204
