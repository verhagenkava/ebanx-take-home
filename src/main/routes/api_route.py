from flask import Blueprint, jsonify, request
from src.main.composer import get_account_composer
from src.main.composer import deposit_account_composer
from src.main.composer import withdraw_account_composer
from src.main.composer import transfer_account_composer
from src.main.adapter import flask_adapter

api_routes_blueprint = Blueprint("api_routes", __name__)


@api_routes_blueprint.route("/balance", methods=["GET"])
def get_account_balance():
    """Get Account Balance Route"""

    response = flask_adapter(request=request, api_route=get_account_composer())

    if response.status_code < 300:

        return str(response.body.balance), response.status_code

    return "0", response.status_code


@api_routes_blueprint.route("/event", methods=["POST"])
def event():
    """Deposit, Withdraw and Transfer Routes"""

    message = {}
    body = request.get_json()

    if body["type"] == "deposit":
        response = flask_adapter(request=request, api_route=deposit_account_composer())

        if response.status_code < 300:
            message = {"id": str(response.body.id), "balance": response.body.balance}

            return jsonify({"destination": message}), response.status_code

        return "0", response.status_code

    if body["type"] == "withdraw":
        response = flask_adapter(request=request, api_route=withdraw_account_composer())

        if response.status_code < 300:
            message = {"id": str(response.body.id), "balance": response.body.balance}

            return jsonify({"origin": message}), response.status_code

        return "0", response.status_code

    if body["type"] == "transfer":
        response = flask_adapter(request=request, api_route=transfer_account_composer())

        if response.status_code < 300:
            origin_message = {
                "id": str(response.body[0].id),
                "balance": response.body[0].balance,
            }

            destination_message = {
                "id": str(response.body[1].id),
                "balance": response.body[1].balance,
            }

            return (
                jsonify({"origin": origin_message, "destination": destination_message}),
                response.status_code,
            )

        return "0", response.status_code

    return jsonify({"data": message}), 200
