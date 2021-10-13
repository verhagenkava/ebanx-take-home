from faker import Faker
from src.infra.test import AccountRepositoryMock
from src.data.test import GetAccountMock
from .transfer import TransferAccount

faker = Faker()


def test_transfer_from_existing_account_to_new_account():
    """Test from existing account to new account transfer method"""

    account_repository = AccountRepositoryMock()
    get_account = GetAccountMock(account_repository)
    transfer_account = TransferAccount(account_repository, get_account)

    attributes = {
        "origin_account_id": 100,
        "destination_account_id": faker.random_number(digits=3),
        "amount": 100.0,
    }

    response = transfer_account.transfer(
        origin_account_id=attributes["origin_account_id"],
        destination_account_id=attributes["destination_account_id"],
        amount=attributes["amount"],
    )

    assert (
        account_repository.update_account_params["account_id"]
        == attributes["origin_account_id"]
    )
    assert (
        account_repository.update_account_params["balance"]
        == get_account.account_balance_param["balance"] - attributes["amount"]
    )
    assert (
        account_repository.create_account_params["account_id"]
        == attributes["destination_account_id"]
    )
    assert account_repository.create_account_params["balance"] == attributes["amount"]

    assert (
        get_account.account_id_param["account_id"]
        == attributes["destination_account_id"]
    )

    assert response["Success"] is True
    assert response["Data"]
