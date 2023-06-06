from typing import List
from api.models.professional_model import ProfessionalModel
# from api.schemas.professional_schema import ProfessionalSchema
from api.dtos.professional_dto import ProfessionalDTO
from api import db


class ProfessionalService:
    @staticmethod
    async def get_all_professionals() -> List[ProfessionalModel]:
        professionals = await db.session.query(ProfessionalModel).all()
        return professionals

    @staticmethod
    async def get_professional(professional_id: int) -> ProfessionalModel:
        professional = await db.session.query(ProfessionalModel).get_or_404(professional_id)
        return professional

    @staticmethod
    async def create_professional(professional_dto: ProfessionalDTO) -> ProfessionalModel:
        professional = ProfessionalModel(**professional_dto.dict())

        async with db.session.begin():
            db.session.add(professional)
            await db.session.commit()

        return professional

    @staticmethod
    async def update_professional(professional_id: int, professional_dto: ProfessionalDTO) -> ProfessionalModel:
        professional = await db.session.query(ProfessionalModel).get_or_404(professional_id)

        professional.name = professional_dto.name
        professional.project = professional_dto.project
        professional.responsible = professional_dto.responsible
        professional.work_experience = professional_dto.work_experience
        professional.level = professional_dto.level
        professional.hour_value = professional_dto.hour_value
        professional.salary = professional_dto.salary
        professional.current_work = professional_dto.current_work
        professional.to_be_rated = professional_dto.to_be_rated
        professional.data_created = professional_dto.data_created

        async with db.session.begin():
            await db.session.commit()

        return professional

    @staticmethod
    async def delete_professional(professional_id: int):
        professional = await db.session.query(ProfessionalModel).get_or_404(professional_id)

        async with db.session.begin():
            db.session.delete(professional)
            await db.session.commit()
