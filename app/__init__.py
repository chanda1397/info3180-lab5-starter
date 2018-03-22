from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = "change this to be a more random key"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgres://emjhntpucdeygb:3052609067d7c5a3a1cf8984471a2eea2aff9919a7bece9975566bf56604345b@ec2-23-21-217-27.compute-1.amazonaws.com:5432/d5ja0fee4fu9lu"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # added just to suppress a warning

db = SQLAlchemy(app)


UPLOAD_FOLDER ='./app/static/uploads'



app.config.from_object(__name__)
from app import views
