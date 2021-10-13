from typing import Type
from src.main.interface import RouteInterface
from src.domain.use_cases import DepositAccount
from src.presenters.helpers import HttpRequest, HttpResponse
from src.presenters.errors import HttpErrors


class DepositAccountController(RouteInterface):
    """Deposit in Account use case controller"""

    def __init__(self, deposit_account_use_case: Type[DepositAccount]):
        self.deposit_account_use_case = deposit_account_use_case

    def route(self, http_request: Type[HttpRequest]) -> HttpResponse:
        """Method to call use case"""

        response = None

        if http_request.body:

            body_params = http_request.body.keys()

            if "destination" in body_params and "amount" in body_params:
                account_id = int(http_request.body["destination"])
                amount = float(http_request.body["amount"])

                response = self.deposit_account_use_case.deposit(
                    account_id=account_id, amount=amount
                )
            else:
                response = {"Success": False, "Data": None}

            if response["Success"] is False:
                https_error = HttpErrors.error_400()
                return HttpResponse(
                    status_code=https_error["status_code"], body=https_error["body"]
                )

            return HttpResponse(status_code=201, body=response["Data"])

        https_error = HttpErrors.error_400()
        return HttpResponse(
            status_code=https_error["status_code"], body=https_error["body"]
        )
