from flask_restful import Api


import routes

from init_app import app


api = Api(app)

api.add_resource(
    routes.TaskAPI,
    '/tasks/<int:t_id>'
)

api.add_resource(
    routes.TaskListAPI,
    '/tasks',
)

api.add_resource(
    routes.StatusAPI,
    '/statuses',
)

if __name__ == '__main__':
    app.run(debug=True)
