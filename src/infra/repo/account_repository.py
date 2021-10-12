from collections import namedtuple
from src.domain.models import Accounts
from src.infra.config import DBConnectionHandler
from src.infra.entities import Accounts as AccountsModel


class AccountRepository:
    """Account Repository Manager"""

    @classmethod
    def create_account(cls, account_id: int, balance: float) -> Accounts:
        """Method for inserting data in account entity
        :params - id: Account id
                - balance: Account balance
        :return - Tuple with new account information"""

        InsertedData = namedtuple("Accounts", "id balance")

        with DBConnectionHandler() as db_connection:
            try:
                new_account = AccountsModel(id=account_id, balance=balance)
                db_connection.session.add(new_account)
                db_connection.session.commit()

                return InsertedData(id=new_account.id, balance=new_account.balance)
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()
