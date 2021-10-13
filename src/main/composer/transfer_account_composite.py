from src.presenters.controllers import TransferAccountController
from src.data.transfer_account import TransferAccount
from src.data.get_account import GetAccount
from src.infra.repo.account_repository import AccountRepository


def transfer_account_composer() -> TransferAccountController:
    """Composing Deposit Account Route
    :param - None
    :return - Object with Get Account Route
    """

    repository = AccountRepository()
    get_account = GetAccount(repository)
    use_case = TransferAccount(repository, get_account)
    transfer_account_route = TransferAccountController(use_case)

    return transfer_account_route
