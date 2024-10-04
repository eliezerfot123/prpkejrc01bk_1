# -*- coding: utf-8 -*-
"""User views."""
import jwt
from flask import Blueprint, request, jsonify
from qaroni.logs import log_info
from qaroni.handler_error import HandlerException
from apps.books.models import Books
from apps.books.controllers import BooksController


books_blueprint_api = Blueprint("books", __name__)


@books_blueprint_api.route("/api/books/", methods=["GET"])
def get_books():
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
          id: SimpleResponseSchema
          properties:
            statusResponse:
              type: object
              properties:
                statusCode:
                  type: string
                  description: Response code
                  default: "200"
                status:
                  type: string
                  description: Response message

    """
    try:
        #books = Books().get_all()
        ctrl = BooksController()
        books = ctrl.execute()

        return jsonify({
            "message": "successfully retrieved all books",
            "data": books
        })
    except Exception as e:
        return jsonify({
            "message": "failed to retrieve all books",
            "error": str(e),
            "data": None
        }), 500


