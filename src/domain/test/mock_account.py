from faker import Faker
from src.domain.models import Accounts

faker = Faker()


def mock_account(
    account_id: int = faker.random_number(digits=3), min_value: float = 10.0
) -> Accounts:
    """Mocking Account"""

    return Accounts(
        id=account_id,
        balance=faker.pyfloat(positive=True, min_value=min_value, max_value=5000.0),
    )
