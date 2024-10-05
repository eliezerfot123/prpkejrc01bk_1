# -*- coding: utf-8 -*-
"""User views."""
import jwt
from flask import Blueprint, jsonify, request
from flask_jwt_extended import create_access_token, jwt_required

from apps.user.controllers import LoginUserController, RegisterUserController
from apps.user.models import User
from qaroni.handler_error import HandlerException
from qaroni.logs import log_info

users_blueprint_api = Blueprint("users", __name__)


@users_blueprint_api.route("/api/accounts/register/", methods=["POST"])
def register():
    """Register user
    ---
    tags:
      - Register user

    parameters:
    - in: body
      name: body
      description: User data
      schema:
        properties:
          email:
            type: string
          password:
            type: string
          first_name:
            type: string
          last_name:
            type: string
          type:
            type: string
            enum:
              - director
              - librarians
        example:
          email: 9HsZB@example.com
          password: password
          first_name: John
          last_name: Doe
          type: director

    responses:
      200:
        message: Success
        schema:
          id: SimpleResponseSchema
          properties:
            message:
              type: string
            200:
              type: object
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
    """Login user
    ---
    tags:
      - Login user

    parameters:
    - in: body
      name: body
      description: User data
      schema:
        properties:
          email:
            type: string
          password:
            type: string
        example:
          email: 9HsZB@example.com
          password: password

    responses:
      200:
        message: Success
        schema:
          id: SimpleResponseSchema
          properties:
            message:
              type: string
            200:
              type: object
    """
    email = request.json.get("email")
    password = request.json.get("password")
    data = request.get_json()

    if not email:
        return jsonify({"message": "Email is required"}), 400
    if not password:
        return jsonify({"message": "Password is required"}), 400

    call = LoginUserController()
    result = call.execute(data)
    if not result:
        return jsonify({"message": "Invalid credentials"}), 400
    else:
        access_token = create_access_token(identity=email)
        return jsonify({"access_token": access_token}), 200


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
