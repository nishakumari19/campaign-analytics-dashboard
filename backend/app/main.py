from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware  # 🔥 Import this
from . import models, database
from app.seed import seed_data
from contextlib import asynccontextmanager

models.Base.metadata.create_all(bind=database.engine)

# Define lifespan event
@asynccontextmanager
async def lifespan(app: FastAPI):
    db = database.SessionLocal()
    if db.query(models.Campaign).count() == 0:
        seed_data(db)
    db.close()
    yield

app = FastAPI(lifespan=lifespan)

# 🔥 Add CORS middleware right after app creation
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://campaign-analytics-dashboard-mspetaz47.vercel.app"],  # <-- Replace with your actual Vercel domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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
