# -*- coding: utf-8 -*-
"""User views."""
import io

import pandas as pd
from flask import Blueprint, jsonify, make_response, request
from flask_jwt_extended import jwt_required

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
        # books = Books().get_all()
        ctrl = BooksController()
        books = ctrl.execute()

        return jsonify({"message": "successfully retrieved all books", "data": books})
    except Exception as e:
        return (
            jsonify(
                {
                    "message": "failed to retrieve all books",
                    "error": str(e),
                    "data": None,
                }
            ),
            500,
        )


@books_blueprint_api.route("/api/books/", methods=["POST"])
@jwt_required()
def create_book():
    """
    Create a new book
    ---
    tags:
      - Create book
    consumes:
      - application/json
    parameters:
      - in: body
        name: body
        description: Book data
        schema:
          type: object
          properties:
            title:
              type: string
            description:
              type: string
            image_url:
              type: string
            category:
              type: string
            user_id:
              type: string
            authors:
              type: array
              items:
                type: string
        example:
          title: "Don Quijote de la Mancha"
          description: "Novela del escritor espa ol Miguel de Cervantes"
          image_url: "https://example.com/book.jpg"
          category: "Novela"
          user_id: "8a1b8c9d-0a1b-2c3d-4e5f-6a7b8c9d0a1b"
          authors: ["Miguel de Cervantes Saavedra"]
    responses:
      201:
        message: Book created successfully
        schema:
          id: SimpleResponseSchema
          properties:
            message:
              type: string
      400:
        description: Bad request or missing parameters.
        schema:
          $ref: '#/definitions/ErrorResponseSchema'
    """
    data = request.get_json()
    if not data:
        return jsonify({"message": "No input data provided"}), 400

    ctrl = BooksController()
    result = ctrl.create_data(data)
    if result is None:
        return jsonify({"message": "Book already exists"}), 400

    return jsonify({"message": "Book created successfully"}), 201


@books_blueprint_api.route("/api/books/<int:book_id>/", methods=["PUT"])
@jwt_required()
def update_book(book_id):
    """
    Update a book by id.

    Args:
        book_id (int): Book id

    Returns:
        dict: A dict with a message indicating if the book was updated or not

    Status Codes:
        200 OK: If the book was updated successfully
        400 Bad Request: If the book does not exist

    ---
    tags:
      - Update book
    consumes:
      - application/json
    parameters:
      - in: path
        name: book_id
        description: id of the book
        schema:
          type: integer
        required: true
      - in: body
        name: body
        description: Book data
        schema:
          type: object
          properties:
            title:
              type: string
            description:
              type: string
            image_url:
              type: string
            category:
              type: string
            user_id:
              type: string
            authors:
              type: array
              items:
                type: string
        example:
          title: "Don Quijote de la Mancha"
          description: "Novela del escritor espa ol Miguel de Cervantes"
          image_url: "https://example.com/book.jpg"
          category: "Novela"
          user_id: "8a1b8c9d-0a1b-2c3d-4e5f-6a7b8c9d0a1b"
          authors: ["Miguel de Cervantes Saavedra"]
    responses:
      200:
        message: Book updated successfully
        schema:
          id: SimpleResponseSchema
          properties:
            message:
              type: string
      400:
        description: Bad request or missing parameters.
        schema:
          $ref: '#/definitions/ErrorResponseSchema'
    """
    data = request.get_json()
    if not data:
        return jsonify({"message": "No input data provided"}), 400

    ctrl = BooksController()
    result = ctrl.update_data(book_id, data)
    if result is None or result is False:
        return jsonify({"message": "Book does not exist"}), 400

    return jsonify({"message": "Book updated successfully"}), 200


@books_blueprint_api.route("/api/books/<int:book_id>/", methods=["DELETE"])
@jwt_required()
def delete_book(book_id):
    """
    Delete a book by id.

    Args:
        book_id (int): Book id

    Returns:
        dict: A dict with a message indicating if the book was deleted or not

    Status Codes:
        200 OK: If the book was deleted successfully
        400 Bad Request: If the book does not exist
    ---
    tags:
      - Delete book
    consumes:
      - application/json
    parameters:
      - in: path
        name: book_id
        description: id of the book
        schema:
          type: integer
        required: true
    responses:
      200:
        message: Book deleted successfully
        schema:
          id: SimpleResponseSchema
          properties:
            message:
              type: string
      400:
        description: Bad request or missing parameters.
        schema:
          $ref: '#/definitions/ErrorResponseSchema'
    """
    ctrl = BooksController()
    result = ctrl.delete_data(book_id)
    if result is None or result is False:
        return jsonify({"message": "Book does not exist"}), 400

    return jsonify({"message": "Book deleted successfully"}), 200


@books_blueprint_api.route("/api/books/<int:book_id>/", methods=["GET"])
def get_book(book_id):
    """
    Get book by id
    ---
    tags:
      - Get book by id
    parameters:
    - in: path
      name: book_id
      description: id of the book
      schema:
        type: integer
      required: true
    responses:
      200:
        description: Book retrieved successfully
        schema:
          type: object
      400:
        description: Book does not exist
        schema:
          $ref: '#/definitions/ErrorResponseSchema'
    """
    ctrl = BooksController()
    book = ctrl.get_by_id(book_id)
    if book is None:
        return jsonify({"message": "Book does not exist"}), 400

    return jsonify(book)


@books_blueprint_api.route("/api/export/")
def export_books():
    """
    Export books data to an Excel file.

    This endpoint returns an Excel file (.xlsx) containing the books data
    obtained from the controller.

    Returns:
        HTTP response with Excel file for download
    """
    try:
        # Fetch books data from controller
        ctrl = BooksController()
        books = ctrl.export_data()

        if not books:  # Handle empty data case (optional)
            return jsonify({"message": "No books found for export."}), 404

        # Create DataFrame and BytesIO object
        df = pd.DataFrame(books["books"])
        output = io.BytesIO()

        # Use Pandas' ExcelWriter with 'xlsxwriter' engine
        writer = pd.ExcelWriter(output, engine="xlsxwriter")

        # Write DataFrame to Excel
        df.to_excel(writer, sheet_name="Hoja1", index=False)
        writer._save()  # Correct way to save the workbook

        # Create HTTP response for download
        response = make_response(output.getvalue())
        response.headers["Content-Disposition"] = "attachment; filename=mi_excel.xlsx"
        response.headers["Content-type"] = "application/x-excel"

        return response

    except Exception as e:  # Catch generic exceptions for better error handling
        print(f"An error occurred during export: {e}")
        return (
            jsonify({"message": "An error occurred while exporting Excel."}),
            500,
        )  # Inform user with an appropriate status code
