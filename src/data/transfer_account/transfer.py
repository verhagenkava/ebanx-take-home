from typing import Type, Dict, List
from src.data.get_account import GetAccount
from src.domain.use_cases import TransferAccount as TransferAccountInterface
from src.data.deposit_account import DepositAccount
from src.data.withdraw_account import WithdrawAccount
from src.data.interfaces import AccountRepositoryInterface as AccountRepository
from src.domain.models import Accounts


class TransferAccount(TransferAccountInterface):
    """Transfer account use case class"""

    def __init__(
        self, account_repository: Type[AccountRepository], get_account: Type[GetAccount]
    ):
        self.account_repository = account_repository
        self.get_account = get_account

    def transfer(
        self, origin_account_id: int, destination_account_id: int, amount: float
    ) -> Dict[bool, List[Accounts]]:
        """Transfer account use case
        :params - origin_account_id: Origin Account id
                - destination_account_id: Destination Account id
                - amount: Transfer amount
        :return - Dict with process information"""

        response = None

        validate = (
            isinstance(origin_account_id, int)
            and isinstance(destination_account_id, int)
            and isinstance(amount, float)
        )
        deposit_account = DepositAccount(self.account_repository, self.get_account)
        withdraw_account = WithdrawAccount(self.account_repository, self.get_account)

        if validate:
            withdraw_response = withdraw_account.withdraw(origin_account_id, amount)
            if withdraw_response["Success"]:
                deposit_response = deposit_account.deposit(
                    destination_account_id, amount
                )
                if deposit_response["Success"]:
                    response = [withdraw_response["Data"], deposit_response["Data"]]
                else:
                    {"Success": False, "Data": response}
            else:
                {"Success": False, "Data": response}

        return {"Success": validate, "Data": response}
