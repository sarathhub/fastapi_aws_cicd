from mangum import Mangum
from fastapi import FastAPI, Depends
import api.models
from api.models import Country
from api.database import engine, SessionLocal
from typing import Annotated
from sqlalchemy.orm import Session
from starlette import status
import pyodbc


app = FastAPI()

api.models.Base.metadata.create_all(bind=engine)


@app.get("/")
async def root():
    return {"message": "Hello World from AWS Lambda 13/11/2024"}


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]
@app.get("/countries", status_code=status.HTTP_200_OK)
async def get_countries(db: db_dependency):
    print(pyodbc.drivers())
    return db.query(Country).all()


handler = Mangum(app=app)