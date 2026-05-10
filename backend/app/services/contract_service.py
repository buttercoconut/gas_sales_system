# 간단화된 ContractService 예시
from sqlalchemy.orm import Session
from ..models.contract import ContractCreate, ContractRead, ContractUpdate
from ..database import Base, engine
from sqlalchemy import Column, Integer, String, Date

class ContractORM(Base):
    __tablename__ = "contracts"
    id = Column(Integer, primary_key=True, index=True)
    customer_id = Column(Integer, nullable=False)
    contract_type = Column(String, nullable=False)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=True)
    status = Column(String, nullable=False)

Base.metadata.create_all(bind=engine)

class ContractService:
    @staticmethod
    def create_contract(db: Session, contract: ContractCreate) -> ContractRead:
        db_contract = ContractORM(**contract.dict())
        db.add(db_contract)
        db.commit()
        db.refresh(db_contract)
        return ContractRead.from_orm(db_contract)

    @staticmethod
    def list_contracts(db: Session, skip: int = 0, limit: int = 100):
        contracts = db.query(ContractORM).offset(skip).limit(limit).all()
        return [ContractRead.from_orm(c) for c in contracts]

    @staticmethod
    def get_contract(db: Session, contract_id: int):
        return db.query(ContractORM).filter(ContractORM.id == contract_id).first()

    @staticmethod
    def update_contract(db: Session, contract_id: int, contract: ContractUpdate):
        db_contract = db.query(ContractORM).filter(ContractORM.id == contract_id).first()
        if not db_contract:
            return None
        for key, value in contract.dict(exclude_unset=True).items():
            setattr(db_contract, key, value)
        db.commit()
        db.refresh(db_contract)
        return ContractRead.from_orm(db_contract)

    @staticmethod
    def delete_contract(db: Session, contract_id: int) -> bool:
        db_contract = db.query(ContractORM).filter(ContractORM.id == contract_id).first()
        if not db_contract:
            return False
        db.delete(db_contract)
        db.commit()
        return True
