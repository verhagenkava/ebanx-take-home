from collections import namedtuple
from typing import List
from sqlalchemy.orm.exc import NoResultFound
from src.data.interfaces import AccountRepositoryInterface
from src.domain.models import Accounts
from src.infra.config import DBConnectionHandler
from src.infra.entities import Accounts as AccountsModel


class AccountRepository(AccountRepositoryInterface):
    """Account Repository Manager"""

    @classmethod
    def create_account(cls, account_id: int, balance: float) -> Accounts:
        """Method for inserting data into account entity
        :params - account_id: Account id
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

    @classmethod
    def get_account(cls, account_id: int) -> List[Accounts]:
        """Method for getting data from accounts entity by id
        :param - account_id: Account id
        :return - List with Accounts found"""

        try:
            query_data = None

            if account_id:

                with DBConnectionHandler() as db_connection:
                    data = (
                        db_connection.session.query(AccountsModel)
                        .filter_by(id=account_id)
                        .one()
                    )
                    query_data = [data]

            return query_data

        except NoResultFound:
            return []
        except:
            db_connection.session.rollback()
            raise
        finally:
            db_connection.session.close()

    @classmethod
    def update_account(cls, account_id: int, balance: float) -> Accounts:
        """Method for updating data in accounts entity by id
        :params - account_id: Account id
                - balance: Account balance
        :return - Tuple with updated Account"""

        InsertedData = namedtuple("Accounts", "id balance")

        with DBConnectionHandler() as db_connection:
            try:
                account = (
                    db_connection.session.query(AccountsModel)
                    .filter_by(id=account_id)
                    .one()
                )
                account.balance = balance
                updated_account = (
                    db_connection.session.query(AccountsModel)
                    .filter_by(id=account_id)
                    .one()
                )
                db_connection.session.commit()

                return InsertedData(
                    id=updated_account.id, balance=updated_account.balance
                )
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()
