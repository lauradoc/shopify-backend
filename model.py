"""Model for Shopify Backend challenge"""

# from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# app = Flask(__name__)
db = SQLAlchemy()


class Image(db.Model):
    """Image file and details"""

    __tablename__ = 'images'

    image_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    image_name = db.Column(db.String)
    image_description = db.Column(db.String)
    image_url = db.Column(db.String)


def connect_to_db(flask_app, db_uri='postgresql:///images', echo=False):
    """connect to database"""

    flask_app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    flask_app.config['SQLALCHEMY_ECHO'] = echo
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.app = flask_app
    db.init_app(flask_app)

    print('Connected to the db!')


if __name__ == '__main__':
    from server import app

    connect_to_db(app)
