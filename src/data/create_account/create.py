from typing import Type, Dict
from src.domain.use_cases import CreateAccount as CreateAccountInterface
from src.data.interfaces import AccountRepositoryInterface as AccountRepository
from src.domain.models import Accounts


class CreateAccount(CreateAccountInterface):
    """Create account use case class"""

    def __init__(self, account_repository: Type[AccountRepository]):
        self.account_repository = account_repository

    def create(self, account_id: int, balance: float) -> Dict[bool, Accounts]:
        """Create account use case
        :params - account_id: Account id
                - balance: Account balance
        :return - Dict with process information"""

        response = None
        validate = isinstance(account_id, int) and isinstance(balance, float)

        if validate:
            response = self.account_repository.create_account(account_id, balance)

        return {"Success": validate, "Data": response}
