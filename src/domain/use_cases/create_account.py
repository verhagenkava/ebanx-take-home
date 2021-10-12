from abc import ABC, abstractmethod
from typing import Dict
from src.domain.models import Accounts


class CreateAccount(ABC):
    """Interface for Create Account use case"""

    @abstractmethod
    def create(self, account_id: int, balance: float) -> Dict[bool, Accounts]:
        """Create Account use case"""
        raise Exception("Method should be implemented")
