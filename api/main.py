from mangum import Mangum
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World from AWS Lambda"}


@app.get("/test")
async def my_test():
    return {"message": "test from AWS Lambda"}


handler = Mangum(app=app)