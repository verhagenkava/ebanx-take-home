from sqlalchemy import Column, Integer, Float
from src.infra.config import Base


class Accounts(Base):
    """Accounts Entity"""

    __tablename__ = "accounts"

    id = Column(Integer, primary_key=True)
    balance = Column(Float, nullable=False)

    def __repr__(self) -> str:
        return f"Account [id={self.id}]"
