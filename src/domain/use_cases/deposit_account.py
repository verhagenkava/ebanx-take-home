from abc import ABC, abstractmethod
from typing import Dict
from src.domain.models import Accounts


class DepositAccount(ABC):
    """Interface for Deposit Account use case"""

    @abstractmethod
    def deposit(self, account_id: int, amount: float) -> Dict[bool, Accounts]:
        """Deposit Account use case"""
        raise Exception("Method should be implemented")
