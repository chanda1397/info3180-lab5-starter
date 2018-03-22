from flask import Flask

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = "change this to be a more random key"
app.config['SQLALCHEMY_DATABASE_URI'] =  'postgresql://xsywcgiromherd:a0bf8466d3f88e12a27bfeba16e6496e3c248b92e8a7ab7a48c8953a1d60eb27@ec2-23-21-217-27.compute-1.amazonaws.com:5432/dcqreahlb0hupu'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # added just to suppress a warning

db = SQLAlchemy(app)


UPLOAD_FOLDER ='./app/static/uploads'




app.config.from_object(__name__)
from app import views
