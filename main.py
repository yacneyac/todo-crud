# from flask import Flask
from flask_restful import Api


import routes

from init_app import app


# app = Flask(__name__)
api = Api(app)

api.add_resource(
    routes.TodoAPI,
    '/todos/<int:t_id>'
)

api.add_resource(
    routes.TodoListAPI,
    '/todos',
)

api.add_resource(
    routes.StatusAPI,
    '/statuses',
)

if __name__ == '__main__':
    app.run(debug=True)
