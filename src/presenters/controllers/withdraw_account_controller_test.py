from faker import Faker
from src.data.test import GetAccountMock
from src.infra.test import AccountRepositoryMock
from src.presenters.helpers import HttpRequest
from src.data.withdraw_account import WithdrawAccount
from .withdraw_account_controller import WithdrawAccountController


faker = Faker()


def test_route_existing_account():
    """Testing Route method for withdraw from existing account use case"""

    account_repository = AccountRepositoryMock()
    get_account = GetAccountMock(account_repository)
    withdraw_account = WithdrawAccount(account_repository, get_account)
    withdraw_account_controller = WithdrawAccountController(withdraw_account)

    attributes = {
        "type": "withdraw",
        "origin": "100",
        "amount": faker.random_number(digits=3),
    }

    response = withdraw_account_controller.route(HttpRequest(body=attributes))

    assert get_account.account_id_param["account_id"] == int(attributes["origin"])
    assert account_repository.update_account_params["account_id"] == int(
        attributes["origin"]
    )

    assert (
        account_repository.update_account_params["balance"]
        == get_account.account_balance_param["balance"] - attributes["amount"]
    )

    assert response.status_code == 201
    assert response.body


def test_route_non_existing_account():
    """Testing Route method for withdraw from account use case non existing account"""

    account_repository = AccountRepositoryMock()
    get_account = GetAccountMock(account_repository)
    withdraw_account = WithdrawAccount(account_repository, get_account)
    withdraw_account_controller = WithdrawAccountController(withdraw_account)

    attributes = {
        "type": "withdraw",
        "origin": faker.random_number(digits=2),
        "amount": faker.random_number(digits=3),
    }

    response = withdraw_account_controller.route(HttpRequest(body=attributes))

    assert get_account.account_id_param["account_id"] == int(attributes["origin"])

    assert response.status_code == 404
    assert "error" in response.body
