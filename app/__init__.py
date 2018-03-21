from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = "change this to be a more random key"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://mpgvrkrqnckffk:93895d6c9835cf31b25117b2398f7eef9282705a713f1c49209f8d48848090f8@ec2-54-204-44-140.compute-1.amazonaws.com:5432/d2an6pdbadqd42"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # added just to suppress a warning

db = SQLAlchemy(app)


UPLOAD_FOLDER ='./app/static/uploads'



app.config.from_object(__name__)
from app import views
