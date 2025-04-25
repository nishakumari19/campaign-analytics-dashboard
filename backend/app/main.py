from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from . import models, database

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/campaigns")
def read_campaigns(db: Session = Depends(get_db)):
    return db.query(models.Campaign).all()
