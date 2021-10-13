from src.presenters.controllers import WithdrawAccountController
from src.data.withdraw_account import WithdrawAccount
from src.data.get_account import GetAccount
from src.infra.repo.account_repository import AccountRepository


def withdraw_account_composer() -> WithdrawAccountController:
    """Composing Withdraw Account Route
    :param - None
    :return - Object with Get Account Route
    """

    repository = AccountRepository()
    get_account = GetAccount(repository)
    use_case = WithdrawAccount(repository, get_account)
    withdraw_account_route = WithdrawAccountController(use_case)

    return withdraw_account_route
