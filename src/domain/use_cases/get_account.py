from abc import ABC, abstractmethod
from typing import Dict
from src.domain.models import Accounts


class GetAccount(ABC):
    """Interface for Get Account use case"""

    @abstractmethod
    def get(self, account_id: int) -> Dict[bool, Accounts]:
        """Get Account use case"""
        raise Exception("Method should be implemented")
