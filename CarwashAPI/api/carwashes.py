from fastapi import APIRouter, Query
from CarwashAPI.services.filter_by_time import filter_by_time
from CarwashAPI.services.filter_by_service import filter_by_service
from CarwashAPI.services.filter_by_name import filter_by_name
from CarwashAPI.db.database import carwashes  # пока фейковые данные
from CarwashAPI.schemas.carwash import CarWashOut

router = APIRouter(
    prefix="/carwashes",
    tags=["Carwashes"]
)

@router.get("/", response_model=list[CarWashOut])
def get_filtered_carwashes(
    name: str = Query(None),
    time: str = Query(None),
    service: str = Query(None)
):
    result = carwashes

    if name:
        result = filter_by_name(result, name)

    if time:
        result = filter_by_time(result, time)

    if service:
        result = filter_by_service(result, service)

    return result