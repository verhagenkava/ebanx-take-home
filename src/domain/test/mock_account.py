from faker import Faker
from src.domain.models import Accounts

faker = Faker()


def mock_account(min_value: float = 10.0) -> Accounts:
    """Mocking Account"""

    return Accounts(
        id=faker.random_number(digits=3),
        balance=faker.pyfloat(positive=True, min_value=min_value, max_value=5000.0),
    )
