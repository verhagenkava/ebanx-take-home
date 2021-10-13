from src.presenters.controllers import DepositAccountController
from src.data.deposit_account import DepositAccount
from src.data.get_account import GetAccount
from src.infra.repo.account_repository import AccountRepository


def deposit_account_composer() -> DepositAccountController:
    """Composing Deposit Account Route
    :param - None
    :return - Object with Get Account Route
    """

    repository = AccountRepository()
    get_account = GetAccount(repository)
    use_case = DepositAccount(repository, get_account)
    deposit_account_route = DepositAccountController(use_case)

    return deposit_account_route
