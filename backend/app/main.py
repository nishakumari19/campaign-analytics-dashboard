from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from . import models, database
from app.seed import seed_data
from contextlib import asynccontextmanager

models.Base.metadata.create_all(bind=database.engine)

# Define lifespan event
@asynccontextmanager
async def lifespan(app: FastAPI):
    db = database.SessionLocal()
    seed_data(db)
    db.close()
    yield

app = FastAPI(lifespan=lifespan)

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/campaigns")
def read_campaigns(db: Session = Depends(get_db)):
    return db.query(models.Campaign).all()

@app.post("/seed")
def seed_database(db: Session = Depends(get_db)):
    seed_data(db)
    return {"message": "Database seeded successfully"}
