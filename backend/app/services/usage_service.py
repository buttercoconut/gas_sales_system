# 간단화된 UsageService 예시
from sqlalchemy.orm import Session
from ..models.usage_data import UsageCreate, UsageRead
from ..database import Base, engine
from sqlalchemy import Column, Integer, Float, String, Date

class UsageORM(Base):
    __tablename__ = "usage_data"
    id = Column(Integer, primary_key=True, index=True)
    contract_id = Column(Integer, nullable=False)
    usage_date = Column(Date, nullable=False)
    volume = Column(Float, nullable=False)
    unit = Column(String, nullable=False)

Base.metadata.create_all(bind=engine)

class UsageService:
    @staticmethod
    def record_usage(db: Session, usage: UsageCreate) -> UsageRead:
        db_usage = UsageORM(**usage.dict())
        db.add(db_usage)
        db.commit()
        db.refresh(db_usage)
        return UsageRead.from_orm(db_usage)

    @staticmethod
    def list_usages(db: Session, skip: int = 0, limit: int = 100):
        usages = db.query(UsageORM).offset(skip).limit(limit).all()
        return [UsageRead.from_orm(u) for u in usages]

    @staticmethod
    def get_usage(db: Session, usage_id: int):
        return db.query(UsageORM).filter(UsageORM.id == usage_id).first()
