from flask import request, make_response
from flask_restful import Resource, abort
from api.schemes.professional_scheme import ProfessionalSchema
from marshmallow import ValidationError
from sqlalchemy.orm.exc import NoResultFound

from api.dtos.professional_dto import ProfessionalDTO
from api import db
from api.models.professional_model import ProfessionalModel

professional_schema = ProfessionalSchema()
professionals_schema = ProfessionalSchema(many=True)


class ProfessionalResource(Resource):
    def get(self):
        try:
            professionals = ProfessionalModel.query.all()
            return professionals_schema.dump(professionals), 200
        except ValidationError as error:
            abort(500, message=error.messages)

    def post(self):
        professional_dto = None  # Inicialização da variável com None
        try:
            professional_dto = professional_schema.load(request.json)
        except ValidationError as error:
            abort(400, message=error.messages)

        professional = ProfessionalModel(**professional_dto)

        db.session.add(professional)
        db.session.commit()

        return professional_schema.dump(professional), 201


class ProfessionalDetailResource(Resource):
    def get(self, professional_id):
        professional = ProfessionalModel.query.filter_by(id=professional_id).first()
        if professional:
            return professional_schema.dump(professional), 200
        else:
            abort(404, message=f"Professional with id {professional_id} not found")

    def put(self, professional_id):
        professional_dto = None  # Inicialização da variável com None
        try:
            professional_dto = professional_schema.load(request.json)
        except ValidationError as error:
            abort(422, message=error.messages)

        professional = ProfessionalModel.query.get_or_404(professional_id)

        professional.name = professional_dto.get('name', professional.name)
        professional.project = professional_dto.get('project', professional.project)
        professional.responsible = professional_dto.get('responsible', professional.responsible)
        professional.work_experience = professional_dto.get('work_experience', professional.work_experience)
        professional.level = professional_dto.get('level', professional.level)
        professional.hour_value = professional_dto.get('hour_value', professional.hour_value)
        professional.salary = professional_dto.get('salary', professional.salary)
        professional.current_work = professional_dto.get('current_work', professional.current_work)
        professional.to_be_rated = professional_dto.get('to_be_rated', professional.to_be_rated)
        professional.data_created = professional_dto.get('data_created', professional.data_created)

        db.session.commit()

        return professional_schema.dump(professional), 200

    def delete(self, professional_id):
        professional = ProfessionalModel.query.filter_by(id=professional_id).first()
        # professional = ProfessionalModel.query.get_or_404(professional_id)
        if professional:
            db.session.delete(professional)
            db.session.commit()
            message = f"Professional with id {professional_id} removed"
            return message, 200
        else:
            abort(404, message=f"Professional with id {professional_id} not found")



