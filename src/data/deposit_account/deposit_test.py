from faker import Faker
from src.infra.test import AccountRepositoryMock
from src.data.test import GetAccountMock
from .deposit import DepositAccount

faker = Faker()


def test_deposit_new_account():
    """Test for new account deposit method"""

    account_repository = AccountRepositoryMock()
    get_account = GetAccountMock(account_repository)
    deposit_account = DepositAccount(account_repository, get_account)

    attributes = {
        "account_id": faker.random_number(digits=3),
        "amount": faker.pyfloat(positive=True),
    }

    response = deposit_account.deposit(
        account_id=attributes["account_id"], amount=attributes["amount"]
    )

    assert (
        account_repository.create_account_params["account_id"]
        == attributes["account_id"]
    )
    assert account_repository.create_account_params["balance"] == attributes["amount"]

    assert get_account.account_id_param["account_id"] == attributes["account_id"]

    assert response["Success"] is True
    assert response["Data"]


def test_deposit_existing_account():
    """Test for existing account deposit method"""

    account_repository = AccountRepositoryMock()
    get_account = GetAccountMock(account_repository)
    deposit_account = DepositAccount(account_repository, get_account)

    attributes = {
        "account_id": 100,
        "amount": faker.pyfloat(positive=True),
    }

    response = deposit_account.deposit(
        account_id=attributes["account_id"], amount=attributes["amount"]
    )

    assert (
        account_repository.update_account_params["account_id"]
        == attributes["account_id"]
    )
    assert (
        account_repository.update_account_params["balance"]
        == attributes["amount"] + get_account.account_balance_param["balance"]
    )

    assert get_account.account_id_param["account_id"] == attributes["account_id"]

    assert response["Success"] is True
    assert response["Data"]
