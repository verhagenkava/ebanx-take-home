from typing import Type, Dict
from src.domain.use_cases import GetAccount as GetAccountInterface
from src.data.interfaces import AccountRepositoryInterface as AccountRepository
from src.domain.models import Accounts


class GetAccount(GetAccountInterface):
    """Get account use case class"""

    def __init__(self, account_repository: Type[AccountRepository]):
        self.account_repository = account_repository

    def get(self, account_id: int) -> Dict[bool, Accounts]:
        """Get account use case
        :param - account_id: Account id
        :return - Dict with process information"""

        response = None
        validate = isinstance(account_id, int)

        if validate:
            response = self.account_repository.get_account(account_id)

        return {"Success": validate, "Data": response}
