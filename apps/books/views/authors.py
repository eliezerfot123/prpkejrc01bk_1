# -*- coding: utf-8 -*-
"""User views."""
import jwt
from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required

from apps.books.controllers import AuthorsController

authors_blueprint_api = Blueprint("authors", __name__)


@authors_blueprint_api.route("/api/authors/", methods=["GET"])
def get_authors():
    """Get all authors
    ---
    tags:
      - Get authors
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
    ctrl = AuthorsController()
    authors = ctrl.get_all()
    return jsonify(authors)


@authors_blueprint_api.route("/api/authors/", methods=["POST"])
@jwt_required()
def create_author():
    """Create a new author
    ---
    tags:
      - Create author
    consumes:
      - application/json
    parameters:
      - in: body
        name: body
        description: Author data
        schema:
          type: object
          properties:
            name:
              type: string

    responses:
      200:
        message: Author created successfully
        schema:
          type: object
      400:
        message: Author already exists
        schema:
          type: object
    """
    data = request.get_json()
    if not data:
        return jsonify({"message": "No input data provided"}), 400
    ctrl = AuthorsController()
    result = ctrl.create_data(data)
    if result is None:
        return jsonify({"message": "Author already exists"}), 400
    return jsonify({"message": "Author created successfully"})


@authors_blueprint_api.route("/api/authors/<int:author_id>/", methods=["PUT"])
@jwt_required()
def update_author(author_id):
    """Update a author

    Args:
        author_id (int): Author id

    Returns:
        dict: A dict with a message indicating if the author was updated or not

    Status Codes:
        200 OK: If the author was updated successfully
        400 Bad Request: If the author does not exist

    ---
    tags:
      - Update author
    consumes:
      - application/json
    parameters:
      - in: path
        name: author_id
        description: id of the author
        schema:
          type: integer
        required: true
      - in: body
        name: body
        description: Author data
        schema:
          type: object
          properties:
            name:
              type: string

    responses:
      200:
        message: Author updated successfully
        schema:
          type: object
      400:
        message: Author does not exist
        schema:
          type: object
    """
    data = request.get_json()
    if not data:
        return jsonify({"message": "No input data provided"}), 400
    ctrl = AuthorsController()
    result = ctrl.update_data(author_id, data)
    if result is None or result is False:
        return jsonify({"message": "Author does not exist"}), 400
    return jsonify({"message": "Author updated successfully"})


@authors_blueprint_api.route("/api/authors/<int:author_id>/", methods=["DELETE"])
@jwt_required()
def delete_author(author_id):
    """Delete a author

    Args:
        author_id (int): Author id

    Returns:
        dict: A dict with a message indicating if the author was deleted or not

    Status Codes:
        200 OK: If the author was deleted successfully
        400 Bad Request: If the author does not exist

    ---
    tags:
      - Delete author
    consumes:
      - application/json
    parameters:
      - in: path
        name: author_id
        description: id of the author
        schema:
          type: integer
        required: true

    responses:
      200:
        message: Author deleted successfully
        schema:
          type: object
      400:
        message: Author does not exist
        schema:
          type: object
    """
    ctrl = AuthorsController()
    result = ctrl.delete_data(author_id)
    if result is None or result is False:
        return jsonify({"message": "Author does not exist"}), 400
    return jsonify({"message": "Author deleted successfully"})


@authors_blueprint_api.route("/api/authors/<int:author_id>/", methods=["GET"])
def get_author(author_id):
    """Get author by id

    Args:
        author_id (int): Author id

    Returns:
        dict: A dict with the author data

    Status Codes:
        200 OK: If the author was retrieved successfully
        400 Bad Request: If the author does not exist

    ---
    tags:
      - Get author
    consumes:
      - application/json
    parameters:
      - in: path
        name: author_id
        description: id of the author
        schema:
          type: integer
        required: true

    responses:
      200:
        description: Author retrieved successfully
        schema:
          type: object
      400:
        description: Author does not exist
        schema:
          $ref: '#/definitions/ErrorResponseSchema'
    """
    ctrl = AuthorsController()
    author = ctrl.get_by_id(author_id)
    if author is None:
        return jsonify({"message": "Author does not exist"}), 400
    return jsonify(author)
