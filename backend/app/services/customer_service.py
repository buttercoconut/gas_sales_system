# 서비스 레이어 예시 (간단화)
from sqlalchemy.orm import Session
from ..models.customer import CustomerCreate, CustomerRead, CustomerUpdate
from ..database import Base, engine
from sqlalchemy import Column, Integer, String

# ORM 모델 정의 (예시)
class CustomerORM(Base):
    __tablename__ = "customers"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    phone = Column(String, nullable=True)
    address = Column(String, nullable=True)

# 테이블 생성
Base.metadata.create_all(bind=engine)

class CustomerService:
    @staticmethod
    def create_customer(db: Session, customer: CustomerCreate) -> CustomerRead:
        db_customer = CustomerORM(**customer.dict())
        db.add(db_customer)
        db.commit()
        db.refresh(db_customer)
        return CustomerRead.from_orm(db_customer)

    @staticmethod
    def list_customers(db: Session, skip: int = 0, limit: int = 100):
        customers = db.query(CustomerORM).offset(skip).limit(limit).all()
        return [CustomerRead.from_orm(c) for c in customers]

    @staticmethod
    def get_customer(db: Session, customer_id: int):
        return db.query(CustomerORM).filter(CustomerORM.id == customer_id).first()

    @staticmethod
    def update_customer(db: Session, customer_id: int, customer: CustomerUpdate):
        db_customer = db.query(CustomerORM).filter(CustomerORM.id == customer_id).first()
        if not db_customer:
            return None
        for key, value in customer.dict(exclude_unset=True).items():
            setattr(db_customer, key, value)
        db.commit()
        db.refresh(db_customer)
        return CustomerRead.from_orm(db_customer)

    @staticmethod
    def delete_customer(db: Session, customer_id: int) -> bool:
        db_customer = db.query(CustomerORM).filter(CustomerORM.id == customer_id).first()
        if not db_customer:
            return False
        db.delete(db_customer)
        db.commit()
        return True
