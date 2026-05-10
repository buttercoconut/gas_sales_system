# 간단화된 PaymentService 예시
from sqlalchemy.orm import Session
from ..models.payment import PaymentCreate, PaymentRead
from ..database import Base, engine
from sqlalchemy import Column, Integer, Float, String, Date

class PaymentORM(Base):
    __tablename__ = "payments"
    id = Column(Integer, primary_key=True, index=True)
    contract_id = Column(Integer, nullable=False)
    amount = Column(Float, nullable=False)
    payment_date = Column(Date, nullable=False)
    method = Column(String, nullable=False)

Base.metadata.create_all(bind=engine)

class PaymentService:
    @staticmethod
    def create_payment(db: Session, payment: PaymentCreate) -> PaymentRead:
        db_payment = PaymentORM(**payment.dict())
        db.add(db_payment)
        db.commit()
        db.refresh(db_payment)
        return PaymentRead.from_orm(db_payment)

    @staticmethod
    def list_payments(db: Session, skip: int = 0, limit: int = 100):
        payments = db.query(PaymentORM).offset(skip).limit(limit).all()
        return [PaymentRead.from_orm(p) for p in payments]

    @staticmethod
    def get_payment(db: Session, payment_id: int):
        return db.query(PaymentORM).filter(PaymentORM.id == payment_id).first()
