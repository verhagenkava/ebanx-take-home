from typing import Dict
from faker import Faker
from src.domain.models import Accounts
from src.domain.test import mock_account

faker = Faker()


class GetAccountMock:
    """Mock for getting account use case"""

    def __init__(self, account_repository: any):
        self.account_repository = account_repository
        self.account_id_param = {}
        self.account_balance_param = {}

    def get(self, account_id: int) -> Dict[bool, Accounts]:
        """Get Account by id"""

        self.account_id_param["account_id"] = account_id
        response = None
        validate = isinstance(account_id, int) and account_id == 100

        if validate:
            response = mock_account(min_value=100.0)
            self.account_balance_param["balance"] = response.balance

        return {"Success": validate, "Data": response}
