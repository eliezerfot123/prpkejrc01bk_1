# -*- coding: utf-8 -*-
"""User views."""
import jwt
from flask import Blueprint, request, jsonify
from qaroni.logs import log_info
from apps.user.controllers import RegisterUserController, LoginUserController
from qaroni.handler_error import HandlerException
from apps.user.models import User
from flask_jwt_extended import create_access_token


users_blueprint_api = Blueprint("users", __name__)


@users_blueprint_api.route("/api/accounts/register/", methods=["POST"])
def register():
    """Get service status
    ---
    tags:
      - Get service status
    parameters:
    - name: fintechid
      in: header
      type: string
      required: true
      description: The ID of fintech
    - name: bank
      in: query
      type: string
      required: true
      description: The ID of bank
    - name: services
      in: query
      type: string
      required: true
      description: service that allows interaction
    - name: event
      in: query
      type: string
      required: true
      description: event create for the services
    responses:
      200:
        description: Success. Status of services
        schema:
          $ref: '#/definitions/SimpleResponseSchema'
      400:
        description: Bad request or missing parameters.
        schema:
          $ref: '#/definitions/ErrorResponseSchema'
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
        return HandlerException.STATUS400_DATA_NOT_FOUND(
            "type must be director or librarians"
        )

    ctrl = RegisterUserController()
    result = ctrl.execute(data)
    if result is None:
        return HandlerException.STATUS400_DATA_NOT_FOUND("User already exists")
    return HandlerException.STATUS200(result)



@users_blueprint_api.route("/api/accounts/login/", methods=["POST"])
def login():
    email = request.json.get('email')
    password = request.json.get('password')
    data = request.get_json()

    if not email:
        return jsonify({'message': 'Email is required'}), 400
    if not password:
        return jsonify({'message': 'Password is required'}), 400
    
    call = LoginUserController()
    result = call.execute(data)
    if not result:
        return jsonify({'message': 'Invalid credentials'}), 400
    else:
        access_token = create_access_token(identity=email)
        return jsonify({'access_token': access_token}), 200




@users_blueprint_api.route("/actuator/health", methods=["GET"])
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
        result="UP",
    )
    if data:
        print("Result:", data)
    return {"status": "UP"}
