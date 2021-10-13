from typing import Type, Dict
from src.data.get_account import GetAccount
from src.domain.use_cases import WithdrawAccount as WithdrawAccountInterface
from src.data.interfaces import AccountRepositoryInterface as AccountRepository
from src.domain.models import Accounts


class WithdrawAccount(WithdrawAccountInterface):
    """Withdraw account use case class"""

    def __init__(
        self, account_repository: Type[AccountRepository], get_account: Type[GetAccount]
    ):
        self.account_repository = account_repository
        self.get_account = get_account

    def withdraw(self, account_id: int, amount: float) -> Dict[bool, Accounts]:
        """Withdraw account use case
        :params - account_id: Account id
                - amount: Withdraw amount
        :return - Dict with process information"""

        response = None

        validate = isinstance(account_id, int) and isinstance(amount, float)
        existing_account = self.__get_account(account_id)

        if validate and existing_account["Data"] is not None:
            if amount <= existing_account["Data"].balance:
                new_balance = float(existing_account["Data"].balance - amount)
                response = self.account_repository.update_account(
                    account_id=account_id, balance=new_balance
                )
            else:
                return {"Success": False, "Data": response}
        else:
            return {"Success": False, "Data": response}

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
