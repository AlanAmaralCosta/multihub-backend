from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)
migrate = Migrate(app, db)
api = Api(app)

from api.models import professional_model
from api.resources.professionals_resource import ProfessionalResource, ProfessionalDetailResource

api.add_resource(ProfessionalResource, '/professionals')
api.add_resource(ProfessionalDetailResource, '/professionals/<int:professional_id>')
