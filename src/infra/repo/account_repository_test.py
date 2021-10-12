from faker import Faker
from src.infra.config import DBConnectionHandler
from .account_repository import AccountRepository

faker = Faker()
account_repository = AccountRepository()
db_connection = DBConnectionHandler()


def test_insert_account():
    """Should insert new account"""

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
