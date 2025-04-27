from typing import List
from CarwashAPI.models.carwash import CarWash

def filter_by_name(carwashes: List[CarWash], name: str) -> List[CarWash]:
    return [cw for cw in carwashes if name.lower() in cw.name.lower()]
