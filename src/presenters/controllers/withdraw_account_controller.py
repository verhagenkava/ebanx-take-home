from typing import Type
from src.main.interface import RouteInterface
from src.domain.use_cases import WithdrawAccount
from src.presenters.helpers import HttpRequest, HttpResponse
from src.presenters.errors import HttpErrors


class WithdrawAccountController(RouteInterface):
    """Withdraw in Account use case controller"""

    def __init__(self, withdraw_account_use_case: Type[WithdrawAccount]):
        self.withdraw_account_use_case = withdraw_account_use_case

    def route(self, http_request: Type[HttpRequest]) -> HttpResponse:
        """Method to call use case"""

        response = None

        if http_request.body:

            body_params = http_request.body.keys()

            if "origin" in body_params and "amount" in body_params:
                account_id = int(http_request.body["origin"])
                amount = float(http_request.body["amount"])

                response = self.withdraw_account_use_case.withdraw(
                    account_id=account_id, amount=amount
                )
            else:
                response = {"Success": False, "Data": None}

            if response["Success"] is False:
                https_error = HttpErrors.error_404()
                return HttpResponse(
                    status_code=https_error["status_code"], body=https_error["body"]
                )

            return HttpResponse(status_code=201, body=response["Data"])

        https_error = HttpErrors.error_400()
        return HttpResponse(
            status_code=https_error["status_code"], body=https_error["body"]
        )
