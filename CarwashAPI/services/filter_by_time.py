from typing import List
from CarwashAPI.models.carwash import CarWash  # Модель автомойки

def filter_by_time(carwashes: List[CarWash], desired_time: str) -> List[CarWash]:
    return [cw for cw in carwashes if desired_time in cw.available_times]