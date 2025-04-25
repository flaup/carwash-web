from typing import List

class CarWash:
    def __init__(self, id: int, name: str, available_times: List[str], services: List[str]):
        self.id = id
        self.name = name
        self.available_times = available_times
        self.services = services