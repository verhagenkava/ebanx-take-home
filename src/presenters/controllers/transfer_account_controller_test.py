from faker import Faker
from src.data.test import GetAccountMock
from src.infra.test import AccountRepositoryMock
from src.presenters.helpers import HttpRequest
from src.data.transfer_account import TransferAccount
from .transfer_account_controller import TransferAccountController


faker = Faker()


def test_route_from_existing_account_to_non_existing_account():
    """Testing Route method for transfer from existing account to non existing account"""

    account_repository = AccountRepositoryMock()
    get_account = GetAccountMock(account_repository)
    withdraw_account = TransferAccount(account_repository, get_account)
    transfer_account_controller = TransferAccountController(withdraw_account)

    attributes = {
        "type": "transfer",
        "origin": "100",
        "amount": faker.random_number(digits=3),
        "destination": faker.random_number(digits=2),
    }

    response = transfer_account_controller.route(HttpRequest(body=attributes))

    assert get_account.account_id_param["account_id"] == int(attributes["destination"])
    assert account_repository.update_account_params["account_id"] == int(
        attributes["origin"]
    )

    assert response.status_code == 201
    assert response.body


def test_route_from_non_existing_account():
    """Testing Route method for transfer from non existing account"""

    account_repository = AccountRepositoryMock()
    get_account = GetAccountMock(account_repository)
    withdraw_account = TransferAccount(account_repository, get_account)
    transfer_account_controller = TransferAccountController(withdraw_account)

    attributes = {
        "type": "transfer",
        "origin": faker.random_number(digits=2),
        "amount": faker.random_number(digits=3),
        "destination": faker.random_number(digits=2),
    }

    response = transfer_account_controller.route(HttpRequest(body=attributes))

    assert get_account.account_id_param["account_id"] == int(attributes["origin"])

    assert response.status_code == 404
    assert "error" in response.body
