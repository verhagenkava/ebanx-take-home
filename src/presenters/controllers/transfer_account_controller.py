from typing import Type
from src.main.interface import RouteInterface
from src.domain.use_cases import TransferAccount
from src.presenters.helpers import HttpRequest, HttpResponse
from src.presenters.errors import HttpErrors


class TransferAccountController(RouteInterface):
    """Transfer between Account use case controller"""

    def __init__(self, transfer_account_use_case: Type[TransferAccount]):
        self.transfer_account_use_case = transfer_account_use_case

    def route(self, http_request: Type[HttpRequest]) -> HttpResponse:
        """Method to call use case"""

        response = None

        if http_request.body:

            body_params = http_request.body.keys()

            if (
                "destination" in body_params
                and "amount" in body_params
                and "origin" in body_params
            ):
                origin_account_id = int(http_request.body["origin"])
                destination_account_id = int(http_request.body["destination"])
                amount = float(http_request.body["amount"])

                response = self.transfer_account_use_case.transfer(
                    origin_account_id=origin_account_id,
                    destination_account_id=destination_account_id,
                    amount=amount,
                )
            else:
                response = {"Success": False, "Data": None}

            if response["Data"] is None:
                https_error = HttpErrors.error_404()
                return HttpResponse(
                    status_code=https_error["status_code"], body=https_error["body"]
                )

            return HttpResponse(status_code=201, body=response["Data"])

        https_error = HttpErrors.error_400()
        return HttpResponse(
            status_code=https_error["status_code"], body=https_error["body"]
        )
