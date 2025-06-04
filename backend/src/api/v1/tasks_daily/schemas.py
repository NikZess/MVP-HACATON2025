from pydantic import BaseModel
from typing import Annotated
from annotated_types import MinLen, MaxLen

class TaskDailyCreate(BaseModel):
    username: str
    description: Annotated[str, MinLen(3), MaxLen(1000)]
