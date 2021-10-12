from abc import ABC, abstractmethod
from typing import Dict
from src.domain.models import Accounts


class WithdrawAccount(ABC):
    """Interface for Withdraw Account use case"""

    @abstractmethod
    def withdraw(self, account_id: int, amount: float) -> Dict[bool, Accounts]:
        """Withdraw Account use case"""
        raise Exception("Method should be implemented")
