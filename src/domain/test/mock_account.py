from faker import Faker
from src.domain.models import Accounts

faker = Faker()


def mock_account() -> Accounts:
    """Mocking Account"""

    return Accounts(
        id=faker.random_number(digits=3), balance=faker.pyfloat(positive=True)
    )
