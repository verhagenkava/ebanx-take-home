from faker import Faker
from src.data.test import GetAccountMock
from src.infra.test import AccountRepositoryMock
from src.presenters.helpers import HttpRequest
from .get_account_controller import GetAccountController


faker = Faker()


def test_route():
    """Testing Route method for get account use case"""

    get_account = GetAccountMock(AccountRepositoryMock())
    find_user_controller = GetAccountController(get_account)
    http_request = HttpRequest(query={"account_id": 100})

    response = find_user_controller.route(http_request)

    assert (
        get_account.account_id_param["account_id"] == http_request.query["account_id"]
    )

    assert response.status_code == 200
    assert response.body


def test_route_non_existing_account():
    """Testing Route method for get account use case non existing account"""

    get_account = GetAccountMock(AccountRepositoryMock())
    find_user_controller = GetAccountController(get_account)
    http_request = HttpRequest(query={"account_id": faker.random_number(digits=2)})

    response = find_user_controller.route(http_request)

    assert (
        get_account.account_id_param["account_id"] == http_request.query["account_id"]
    )

    assert response.status_code == 404
    assert "error" in response.body
