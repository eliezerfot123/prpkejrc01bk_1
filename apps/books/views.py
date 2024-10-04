# -*- coding: utf-8 -*-
"""User views."""
import jwt
from flask import Blueprint, request, jsonify
from apps.books.controllers import BooksController
from flask_jwt_extended import jwt_required


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


@books_blueprint_api.route('/api/books/', methods=['POST'])
@jwt_required()
def create_book():
    # Lógica para crear un nuevo libro
    
    data = request.get_json()
    if not data:
        return jsonify({'message': 'No input data provided'}), 400
    
    ctrl = BooksController()
    result = ctrl.create_data(data)
    if result is None:
        return jsonify({'message': 'Book already exists'}), 400
    
    return jsonify({'message': 'Book created successfully'}), 201


@books_blueprint_api.route('/api/books/<int:book_id>/', methods=['PUT'])
@jwt_required()
def update_book(book_id):
    # Lógica para actualizar un libro
    
    data = request.get_json()
    if not data:
        return jsonify({'message': 'No input data provided'}), 400
    
    ctrl = BooksController()
    result = ctrl.update_data(book_id, data)
    if result is None or result is False:
        return jsonify({'message': 'Book does not exist'}), 400
    
    return jsonify({'message': 'Book updated successfully'}), 200