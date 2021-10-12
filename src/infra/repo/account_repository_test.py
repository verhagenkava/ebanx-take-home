from faker import Faker
from src.infra.config import DBConnectionHandler
from .account_repository import AccountRepository
from src.infra.entities import Accounts as AccountsModel

faker = Faker()
account_repository = AccountRepository()
db_connection = DBConnectionHandler()


def test_create_account():
    """Should create new account"""

    account_id = faker.random_number(digits=3)
    balance = faker.pyfloat(positive=True)
    engine = db_connection.get_engine()

    new_account = account_repository.create_account(account_id, balance)
    account_query = engine.execute(
        f'SELECT * FROM accounts WHERE id="{new_account.id}";'
    ).fetchone()

    engine.execute(f'DELETE FROM accounts WHERE id="{new_account.id}";')

    assert account_query.id == new_account.id
    assert account_query.balance == new_account.balance


def test_get_account():
    """Should get existing account"""

    account_id = faker.random_number(digits=3)
    balance = faker.pyfloat(positive=True)
    account = AccountsModel(id=account_id, balance=balance)

    engine = db_connection.get_engine()
    engine.execute(
        f'INSERT INTO accounts (id, balance) VALUES ("{account_id}", "{balance}");'
    )

    account_query = account_repository.get_account(account_id=account_id)

    engine.execute(f'DELETE FROM accounts WHERE id="{account_id}";')

    assert account in account_query
