import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/users")
def home():
    return "Test"

if __name__ == "__main__":
    uvicorn.run("main:app", reload= True)