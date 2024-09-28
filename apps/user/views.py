# -*- coding: utf-8 -*-
"""User views."""
from flask import Blueprint, request
from qaroni.logs import log_info
from apps.user.controllers import RegisterUserController
from qaroni.handler_error import HandlerException

users_blueprint_api = Blueprint("users", __name__)


@users_blueprint_api.route("/api/users/register/", methods=["POST"])
def register():
    """
    Register a new user.

    :return: A dictionary containing the status of the registration.
    :rtype: dict
    """
    # validate data from body
    data = request.get_json()

    type_user = ["director", "librarians"]
    if not data:
        return HandlerException.STATUS400_DATA_NOT_FOUND("Data not found")

    if not data.get("email"):
        return HandlerException.STATUS400_DATA_NOT_FOUND("email is required")
    if not data.get("password"):
        return HandlerException.STATUS400_DATA_NOT_FOUND("password is required")
    if not data.get("first_name"):
        return HandlerException.STATUS400_DATA_NOT_FOUND("first_name is required")
    if not data.get("last_name"):
        return HandlerException.STATUS400_DATA_NOT_FOUND("last_name is required")
    if not data.get("type"):
        return HandlerException.STATUS400_DATA_NOT_FOUND("type is required")
    if data.get("type") not in type_user:
        return HandlerException.STATUS400_DATA_NOT_FOUND("type must be director or librarians")
    
    ctrl = RegisterUserController()
    result = ctrl.execute(data)
    if result is None:
        return HandlerException.STATUS400_DATA_NOT_FOUND("User already exists")
    return HandlerException.STATUS200(result)

    
@users_blueprint_api.route("/actuator/health", methods=['GET'])
def actuator():
    """
    Actuator health check.

    Returns "UP" status if the application is healthy.

    :return: A dictionary containing the status of the application.
    :rtype: dict
    """
    data = log_info(
        ip_address=request.remote_addr,
        client=request.environ["HTTP_USER_AGENT"],
        path=request.path,
        result="UP"
    )
    if data:
        print("Result:",data)
    return {"status": "UP"}