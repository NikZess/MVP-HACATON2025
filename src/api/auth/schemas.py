from pydantic import BaseModel
from typing import Annotated
from annotated_types import MinLen, MaxLen

class User(BaseModel):
    username: Annotated[str, MinLen(3), MaxLen(50)]
    password: Annotated[str, MinLen(3), MaxLen(100)]