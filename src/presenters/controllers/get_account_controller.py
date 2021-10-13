from typing import Type
from src.domain.use_cases import GetAccount
from src.presenters.helpers import HttpRequest, HttpResponse
from src.presenters.errors import HttpErrors


class GetAccountController:
    """Get Account use case controller"""

    def __init__(self, get_account_use_case: Type[GetAccount]):
        self.get_account_use_case = get_account_use_case

    def route(self, http_request: Type[HttpRequest]) -> HttpResponse:
        """Method for calling get account use case"""

        response = None

        if http_request.query:
            query_string_params = http_request.query.keys()

            if "account_id" in query_string_params:
                account_id = http_request.query["account_id"]
                response = self.get_account_use_case.get(account_id=account_id)
            else:
                response = {"Success": False, "Data": None}

            if not response["Success"]:
                http_error = HttpErrors.error_404()
                return HttpResponse(
                    status_code=http_error["status_code"], body=http_error["body"]
                )

            return HttpResponse(status_code=200, body=response["Data"])

        http_error = HttpErrors.error_400()
        return HttpResponse(
            status_code=http_error["status_code"], body=http_error["body"]
        )
