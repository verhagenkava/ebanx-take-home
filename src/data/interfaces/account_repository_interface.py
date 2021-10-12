from abc import ABC, abstractmethod
from typing import List
from src.domain.models import Accounts


class AccountRepositoryInterface(ABC):
    """Interface for Account Repository"""

    @abstractmethod
    def create_account(self, account_id: int, balance: float) -> Accounts:
        """Abstract Method for account creation"""

        raise Exception("Method should be implemented")

    @abstractmethod
    def get_account(self, account_id: int) -> List[Accounts]:
        """Abstract Method for getting account"""

        raise Exception("Method should be implemented")

    @abstractmethod
    def update_account(self, account_id: int, balance: float) -> Accounts:
        """Abstract Method for account update"""

        raise Exception("Method should be implemented")
