"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User
from api.utils import generate_sitemap, APIException
from flask_jwt_extended import jwt_required
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity

api = Blueprint('api', __name__)

#JWT authentication
@api.route('/signup', methods=['POST'])
def post_user():
    body = request.get_json(force=True)
    new_user = User(email=body['email'], password=body['password'], username=body['username'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify(new_user.serialize()), 201

@api.route('/login', methods=['POST'])
def login_user():
    body = request.get_json(force=True)
    user = db.session.query(User).filter(User.email == body['email']).first()
    print(user.password)
    if user.password == body['password']:
        access_token = create_access_token(identity={'id': user.id})
        return jsonify(access_token), 200
    else:
        return jsonify('Error user not exist'), 401

@api.route('/private',methods=["GET"])
@jwt_required()
def private():
    user_token=get_jwt_identity()
    user=User.query.get(user_token)
    return jsonify(user.serialize()),200


