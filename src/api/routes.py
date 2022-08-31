"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User, Recipe, Favorite, ShoppingList
from api.utils import generate_sitemap, APIException

api = Blueprint('api', __name__)

#user routes
#Get user 

@api.route('/user', methods=['GET'])
def get_all_user():
    user = User.query.all()
    all_users = list(map(lambda x: x.serialize(), user))
    return jsonify(all_users), 200
    
@api.route('/user/<int:id>', methods=['GET'])
def get_user(id):
    user = User.query.filter_by(id=id).first()
    return jsonify(user.serialize()), 200 


#Post user

@api.route('/user', methods=['POST'])
def post_user():
    user_dictionary = request.json
    user = User()
    user.firstname = user_dictionary['firstname']
    user.lastname = user_dictionary['lastname']
    user.username = user_dictionary['username']
    user.email = user_dictionary['email']
    user.password = user_dictionary['password']
    db.session.add(user)
    db.session.commit()
    user_list= [user.serialize() for user in User.query.all()]
    return jsonify(user_list)

#Delete user

@api.route('/user/<int:id>', methods=['PUT'])
def delete_user(id):
    remove_user = User.query.filter_by(id=id).first()
    print("You sure you want to delete user #:" + str(id))
    db.session.delete(remove_user)
    db.session.commit()
    return jsonify(remove_user.serialize()), 200

#Recipie routes
#Get recipe 

@api.route('/recipe', methods=['GET'])
def get_all_recipes():
    recipe = Recipe.query.all()
    all_recipes = list(map(lambda x: x.serialize(), recipe))
    return jsonify(all_recipes), 200
    
@api.route('/recipe/<int:id>', methods=['GET'])
def get_recipe(id):
    recipe = Recipe.query.filter_by(id=id).first()
    return jsonify(recipe.serialize()), 200 

#Recipe post requests

@api.route('/recipe', methods=['POST'])
def post_recipe():
    recipe_dictionary = request.json
    recipe = Recipe()
    recipe.title = recipe_dictionary['title']
    recipe.servings = recipe_dictionary['servings']
    recipe.ingredients = recipe_dictionary['ingredients']
    recipe.directions = recipe_dictionary['directions']
    db.session.add(recipe)
    db.session.commit()
    recipe_list= [recipe.serialize() for recipe in Recipe.query.all()]
    return jsonify(recipe_list)

#Delete recipe

@api.route('/recipe/<int:id>', methods=['PUT'])
def delete_recipe(id):
    remove_recipe = Recipe.query.filter_by(id=id).first()
    print("You sure you want to delete recipe #:" + id)
    db.session.delete(remove_recipe)
    db.session.commit()
    return jsonify(remove_recipe.serialize()), 200

#Favorite Routes
#Get Favorite

@api.route('/favorites', methods=['GET'])
def get_all_favorites():
    favorite = Favorite.query.all()
    all_favorites = list(map(lambda x: x.serialize(), favorite))
    return jsonify(all_favorites), 200
    
@api.route('/favorite/<int:id>', methods=['GET'])
def get_favorite(id):
    favorite = Favorite.query.filter_by(id=id).first()
    return jsonify(favorite.serialize()), 200 

#Post Favorite 

@api.route('/user/favorite', methods=['POST'])
def create_favorite():
    favorite = request.get_json()
    new_favorite = Favorite(user_id=favorite['user_id'], recipe_id=favorite['recipe_id'], recipe_name=favorite['recipe_name'])
    db.session.add(new_favorite)
    db.session.commit()
    return jsonify(new_favorite.serialize()), 200

#Delete favorite recipe
@api.route('/favorite/recipe/<int:id>', methods=['PUT'])
def delete_favorite(id):
    remove_favorite = favorite.query.filter_by(id=id).first()
    print("You sure you want to delete favorite recipe #:" + id)
    db.session.delete(remove_favorite)
    db.session.commit()
    return jsonify(remove_favorite.serialize()), 200







#jwt authentication
# @api.route('/signup', methods=['POST'])
# def post_user():
#     body = request.get_json(force=True)
#     new_user = User(email=body['email'], password=body['password'], is_active=True)
#     db.session.add(new_user)
#     db.session.commit()
#     return jsonify(new_user.serialize()), 201

# @api.route('/login', methods=['POST'])
# def login_user():
#     body = request.get_json(force=True)
#     user = db.session.query(User).filter(User.email == body['email']).first()
#     print(user.password)
#     if user.password == body['password']:
#         access_token = create_access_token(identity={'id': user.id})
#         return jsonify(access_token), 200
#     else:
#         return jsonify('Error user not exist'), 401

# @api.route('/private',methods=["GET"])
# @jwt_required()
# def private():
#     user_token=get_jwt_identity()
#     user=User.query.get(user_token)
#     return jsonify(user.serialize()),200


    