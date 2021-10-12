from typing import List
from src.domain.models import Accounts
from src.domain.test import mock_account


class AccountRepositoryMock:
    """Mock of Account Repository for testing purpose"""

    def __init__(self):
        self.create_account_params = {}
        self.get_account_params = {}
        self.update_account_params = {}

    def create_account(self, account_id: int, balance: float) -> Accounts:
        """Mock for the attributes"""
        self.create_account_params["account_id"] = account_id
        self.create_account_params["balance"] = balance

        return mock_account()

    def get_account(self, account_id: int) -> List[Accounts]:
        """Mock for the attributes"""
        self.get_account_params["account_id"] = account_id

        return [mock_account]

    def update_account(self, account_id: int, balance: float) -> Accounts:
        """Mock for the attributes"""
        self.update_account_params["account_id"] = account_id
        self.update_account_params["balance"] = balance

        return mock_account()
