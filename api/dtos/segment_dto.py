from pydantic import BaseModel


class SegmentDTO(BaseModel):
    professional_id: int
    segment: str
