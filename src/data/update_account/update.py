from typing import Type, Dict
from src.domain.use_cases import UpdateAccount as UpdateAccountInterface
from src.data.interfaces import AccountRepositoryInterface as AccountRepository
from src.domain.models import Accounts


class UpdateAccount(UpdateAccountInterface):
    """Update account use case class"""

    def __init__(self, account_repository: Type[AccountRepository]):
        self.account_repository = account_repository

    def update(self, account_id: int, balance: float) -> Dict[bool, Accounts]:
        """Update account use case
        :params - account_id: Account id
                - balance: Account balance
        :return - Dict with process information"""

        response = None
        validate = isinstance(account_id, int) and isinstance(balance, float)

        if validate:
            response = self.account_repository.update_account(account_id, balance)

        return {"Success": validate, "Data": response}
