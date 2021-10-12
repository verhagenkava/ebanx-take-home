from abc import ABC, abstractmethod
from typing import Dict
from src.domain.models import Accounts


class UpdateAccount(ABC):
    """Interface for Update Account use case"""

    @abstractmethod
    def update(self, account_id: int, balance: float) -> Dict[bool, Accounts]:
        """Update Account use case"""
        raise Exception("Method should be implemented")
