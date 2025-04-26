from fastapi import FastAPI
from CarwashAPI.api.carwashes import router as carwashes_router

app = FastAPI()


app.include_router(carwashes_router)

@app.get("/users")
def home():
    return "Test"