from faker import Faker
from src.data.test import GetAccountMock
from src.infra.test import AccountRepositoryMock
from src.presenters.helpers import HttpRequest
from src.data.deposit_account import DepositAccount
from .deposit_account_controller import DepositAccountController


faker = Faker()


def test_route_existing_account():
    """Testing Route method for deposit in existing account use case"""

    account_repository = AccountRepositoryMock()
    get_account = GetAccountMock(account_repository)
    deposit_account = DepositAccount(account_repository, get_account)
    deposit_account_controller = DepositAccountController(deposit_account)

    attributes = {
        "type": "deposit",
        "destination": "100",
        "amount": faker.random_number(digits=3),
    }

    response = deposit_account_controller.route(HttpRequest(body=attributes))

    assert get_account.account_id_param["account_id"] == int(attributes["destination"])
    assert account_repository.update_account_params["account_id"] == int(
        attributes["destination"]
    )

    assert response.status_code == 201
    assert response.body


def test_route_non_existing_account():
    """Testing Route method for deposit in account use case non existing account"""

    account_repository = AccountRepositoryMock()
    get_account = GetAccountMock(account_repository)
    deposit_account = DepositAccount(account_repository, get_account)
    deposit_account_controller = DepositAccountController(deposit_account)

    attributes = {
        "type": "deposit",
        "destination": faker.random_number(digits=2),
        "amount": faker.random_number(digits=3),
    }

    response = deposit_account_controller.route(HttpRequest(body=attributes))

    assert get_account.account_id_param["account_id"] == int(attributes["destination"])
    assert account_repository.create_account_params["account_id"] == int(
        attributes["destination"]
    )
    assert account_repository.create_account_params["balance"] == attributes["amount"]

    assert response.status_code == 201
    assert response.body
