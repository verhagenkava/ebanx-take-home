from faker import Faker
from src.infra.test import AccountRepositoryMock
from .get import GetAccount

faker = Faker()


def test_get():
    """Test for getting account method"""

    account_repository = AccountRepositoryMock()
    get_account = GetAccount(account_repository)

    attributes = {"account_id": faker.random_number(digits=3)}

    response = get_account.get(account_id=attributes["account_id"])

    assert (
        account_repository.get_account_params["account_id"] == attributes["account_id"]
    )

    assert response["Success"] is True
    assert response["Data"]


def test_get_failed_validation():
    """Test for failed validation getting account method"""

    account_repository = AccountRepositoryMock()
    get_account = GetAccount(account_repository)

    attributes = {"account_id": faker.name()}

    response = get_account.get(account_id=attributes["account_id"])

    assert account_repository.get_account_params == {}

    assert response["Success"] is False
    assert response["Data"] is None
