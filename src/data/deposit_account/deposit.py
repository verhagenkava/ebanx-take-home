from typing import Type, Dict
from src.data.get_account import GetAccount
from src.domain.use_cases import DepositAccount as DepositAccountInterface
from src.data.interfaces import AccountRepositoryInterface as AccountRepository
from src.domain.models import Accounts


class DepositAccount(DepositAccountInterface):
    """Deposit account use case class"""

    def __init__(
        self, account_repository: Type[AccountRepository], get_account: Type[GetAccount]
    ):
        self.account_repository = account_repository
        self.get_account = get_account

    def deposit(self, account_id: int, amount: float) -> Dict[bool, Accounts]:
        """Deposit account use case
        :params - account_id: Account id
                - amount: Deposit amount
        :return - Dict with process information"""

        response = None

        validate = isinstance(account_id, int) and isinstance(amount, float)
        existing_account = self.__get_account(account_id)

        if validate and not existing_account["Success"]:
            response = self.account_repository.create_account(
                account_id=account_id, balance=amount
            )
        elif validate and existing_account["Success"]:
            new_balance = float(existing_account["Data"].balance + amount)
            response = self.account_repository.update_account(
                account_id=account_id, balance=new_balance
            )

        return {"Success": validate, "Data": response}

    def __get_account(self, account_id: int) -> Dict[bool, Accounts]:
        """Check for existing account
        :param - account_id: Account id
        :return - Dict with existing account information"""

        found_account = None

        if account_id:
            found_account = self.get_account.get(account_id)
        else:
            return {"Success": False, "Data": None}

        return found_account
