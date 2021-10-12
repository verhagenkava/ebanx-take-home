from faker import Faker
from src.infra.test import AccountRepositoryMock
from .create import CreateAccount

faker = Faker()


def test_create():
    """Test for account creation method"""

    account_repository = AccountRepositoryMock()
    create_account = CreateAccount(account_repository)

    attributes = {
        "account_id": faker.random_number(digits=3),
        "balance": faker.pyfloat(positive=True),
    }

    response = create_account.create(
        account_id=attributes["account_id"], balance=attributes["balance"]
    )

    assert (
        account_repository.create_account_params["account_id"]
        == attributes["account_id"]
    )
    assert account_repository.create_account_params["balance"] == attributes["balance"]

    assert response["Success"] is True
    assert response["Data"]


def test_create_failed_validation():
    """Test for failed validation account creation method"""

    account_repository = AccountRepositoryMock()
    create_account = CreateAccount(account_repository)

    attributes = {"account_id": faker.name(), "balance": faker.pyfloat(positive=True)}

    response = create_account.create(
        account_id=attributes["account_id"], balance=attributes["balance"]
    )

    assert account_repository.create_account_params == {}

    assert response["Success"] is False
    assert response["Data"] is None
