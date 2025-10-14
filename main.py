from typing import List
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import models, schemas
from database import SessionLocal, engine, Base
Base.metadata.create_all(bind=engine)


app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/liabilities/", response_model=schemas.LiabilityItem)
def create_liabilityitem(liabilityitem: schemas.LiabilityItemCreate, db: Session = Depends(get_db)):

    db_liabilityitem = models.LiabilityItem(**liabilityitem.dict())
    db.add(db_liabilityitem)
    db.commit()
    db.refresh(db_liabilityitem)
    return db_liabilityitem

@app.get("/liabilities/", response_model=List[schemas.LiabilityItem])
def read_liabilities(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(models.LiabilityItem).offset(skip).limit(limit).all()

@app.get("/")
def read_root():
    return {"message": "FastAPI is working"}

