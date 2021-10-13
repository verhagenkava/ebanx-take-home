from src.presenters.controllers import GetAccountController
from src.data.get_account import GetAccount
from src.infra.repo.account_repository import AccountRepository


def get_account_composer() -> GetAccountController:
    """Composing Get Account Route
    :param - None
    :return - Object with Get Account Route
    """

    repository = AccountRepository()
    use_case = GetAccount(repository)
    get_account_route = GetAccountController(use_case)

    return get_account_route
