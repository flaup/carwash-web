from pydantic import BaseModel
from typing import List

class CarWashOut(BaseModel):
    id: int
    name: str
    available_times: List[str]
    services: List[str]