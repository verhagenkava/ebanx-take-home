from sqlalchemy import Column, Integer, Float
from src.infra.config import Base


class Accounts(Base):
    """Accounts Entity"""

    __tablename__ = "accounts"

    id = Column(Integer, primary_key=True)
    balance = Column(Float, nullable=False)

    def __repr__(self):
        return f"Account [id={self.id}]"

    def __eq__(self, other):
        if self.id == other.id and self.balance == other.balance:
            return True
        return False
