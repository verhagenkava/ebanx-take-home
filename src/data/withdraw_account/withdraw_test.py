from faker import Faker
from src.infra.test import AccountRepositoryMock
from src.data.test import GetAccountMock
from .withdraw import WithdrawAccount

faker = Faker()


def test_withdraw_existing_account():
    """Test for existing account withdraw method"""

    account_repository = AccountRepositoryMock()
    get_account = GetAccountMock(account_repository)
    withdraw_account = WithdrawAccount(account_repository, get_account)

    attributes = {
        "account_id": 100,
        "amount": 100.0,
    }

    response = withdraw_account.withdraw(
        account_id=attributes["account_id"], amount=attributes["amount"]
    )

    assert (
        account_repository.update_account_params["account_id"]
        == attributes["account_id"]
    )
    assert (
        account_repository.update_account_params["balance"]
        == get_account.account_balance_param["balance"] - attributes["amount"]
    )

    assert get_account.account_id_param["account_id"] == attributes["account_id"]

    assert response["Success"] is True
    assert response["Data"]
