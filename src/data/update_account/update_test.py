from faker import Faker
from src.infra.test import AccountRepositoryMock
from .update import UpdateAccount

faker = Faker()


def test_update():
    """Test for account update method"""

    account_repository = AccountRepositoryMock()
    update_account = UpdateAccount(account_repository)

    attributes = {
        "account_id": faker.random_number(digits=3),
        "balance": faker.pyfloat(positive=True),
    }

    response = update_account.update(
        account_id=attributes["account_id"], balance=attributes["balance"]
    )

    assert (
        account_repository.update_account_params["account_id"]
        == attributes["account_id"]
    )
    assert account_repository.update_account_params["balance"] == attributes["balance"]

    assert response["Success"] is True
    assert response["Data"]


def test_update_failed_validation():
    """Test for failed validation account update method"""

    account_repository = AccountRepositoryMock()
    update_account = UpdateAccount(account_repository)

    attributes = {"account_id": faker.name(), "balance": faker.pyfloat(positive=True)}

    response = update_account.update(
        account_id=attributes["account_id"], balance=attributes["balance"]
    )

    assert account_repository.update_account_params == {}

    assert response["Success"] is False
    assert response["Data"] is None
