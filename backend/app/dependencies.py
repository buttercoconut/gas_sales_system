from fastapi import Depends
from sqlalchemy.orm import Session
from ..database import SessionLocal

# DB 세션 의존성

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
