from typing import List
from CarwashAPI.models.carwash import CarWash

def filter_by_service(carwashes: List[CarWash], service: str) -> List[CarWash]:
    return [cw for cw in carwashes if service in cw.services]