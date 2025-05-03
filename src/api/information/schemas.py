from pydantic import BaseModel
from typing import Annotated
from annotated_types import MinLen, MaxLen

class InformationCreate(BaseModel):
    username: Annotated[str, MinLen(3), MaxLen(64)]
    job_title: Annotated[str, MinLen(3), MaxLen(100)]
    work_place: Annotated[str, MinLen(3), MaxLen(50)]
    timetable: Annotated[str, MinLen(3), MaxLen(50)]
    