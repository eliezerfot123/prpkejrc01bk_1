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
    """Get all books
    ---
    tags:
      - Get books
    responses:
      200:
        message: Success. Status of services
        schema:
          id: SimpleResponseSchema
          properties:
            data:
              type: object
            message:
              type: string
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


