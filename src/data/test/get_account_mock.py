from typing import Dict
from src.domain.models import Accounts
from faker import Faker

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
            balance = faker.pyfloat(positive=True, min_value=100.0)
            response = Accounts(id=100, balance=balance)
            self.account_balance_param["balance"] = balance

        return {"Success": validate, "Data": response}
