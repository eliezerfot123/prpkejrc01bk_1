# -*- coding: utf-8 -*-
"""User views."""
import jwt
from flask import Blueprint, request, jsonify
from apps.books.controllers import AuthorsController
from flask_jwt_extended import jwt_required


authors_blueprint_api = Blueprint("authors", __name__)


@authors_blueprint_api.route('/api/authors/', methods=['GET'])
def get_authors():
    ctrl = AuthorsController()
    authors = ctrl.get_all()
    return jsonify(authors)


@authors_blueprint_api.route('/api/authors/', methods=['POST'])
@jwt_required()
def create_author():
    data = request.get_json()
    if not data:
        return jsonify({'message': 'No input data provided'}), 400
    ctrl = AuthorsController()
    result = ctrl.create_data(data)
    if result is None:
        return jsonify({'message': 'Author already exists'}), 400
    return jsonify({'message': 'Author created successfully'})


@authors_blueprint_api.route('/api/authors/<int:author_id>/', methods=['PUT'])
@jwt_required()
def update_author(author_id):
    data = request.get_json()
    if not data:
        return jsonify({'message': 'No input data provided'}), 400
    ctrl = AuthorsController()
    result = ctrl.update_data(author_id, data)
    if result is None or result is False:
        return jsonify({'message': 'Author does not exist'}), 400
    return jsonify({'message': 'Author updated successfully'})


@authors_blueprint_api.route('/api/authors/<int:author_id>/', methods=['DELETE'])
@jwt_required()
def delete_author(author_id):
    ctrl = AuthorsController()
    result = ctrl.delete_data(author_id)
    if result is None or result is False:
        return jsonify({'message': 'Author does not exist'}), 400
    return jsonify({'message': 'Author deleted successfully'})


@authors_blueprint_api.route('/api/authors/<int:author_id>/', methods=['GET'])
def get_author(author_id):
    ctrl = AuthorsController()
    author = ctrl.get_by_id(author_id)
    if author is None:
        return jsonify({'message': 'Author does not exist'}), 400
    return jsonify(author)


