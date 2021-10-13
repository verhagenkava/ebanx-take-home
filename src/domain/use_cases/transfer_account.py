from abc import ABC, abstractmethod
from typing import Dict
from src.domain.models import Accounts


class TransferAccount(ABC):
    """Interface for Transfer Account use case"""

    @abstractmethod
    def transfer(
        self, origin_account_id: int, destination_account_id: int, amount: float
    ) -> Dict[bool, Accounts]:
        """Transfer Account use case"""
        raise Exception("Method should be implemented")
