from flask import Flask
from flask_restful import reqparse
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()
app = Flask(__name__)

# describe the parameters
parser = reqparse.RequestParser()

app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql+psycopg2://db_user:db_pass@localhost/todo_db'
db.init_app(app)


class StatusHTTP:
    OK = 200
    CREATED = 201
    NO_CONTENT = 204
    SERVER_ERROR = 500
    BAD_REQUEST = 400
