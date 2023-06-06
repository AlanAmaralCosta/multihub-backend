from pydantic import BaseModel
from decimal import Decimal


class ProfessionalDTO(BaseModel):
    name: str
    project: str
    responsible: str
    work_experience: int
    level: Decimal
    hour_value: Decimal
    salary: Decimal
    current_work: str
    to_be_rated: bool
    data_created: str
