from flask import Flask
from flask_restful import reqparse
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()
app = Flask(__name__)

# describe the parameters
parser = reqparse.RequestParser(bundle_errors=True)

app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql+psycopg2://db_user:db_pass@localhost/todo_db'
db.init_app(app)
