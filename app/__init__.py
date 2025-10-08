from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.config['SECRET_KEY'] = '276152493yv7n8h2c8fr8234ohsdrn1r8ogrdb8'


db=SQLAlchemy(app)
migrate=Migrate(app, db)

from app import view
from app.model import Questao