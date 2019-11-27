from flask import Blueprint, Flask, request, jsonify
from services.client_service import create_client
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity, get_raw_jwt
from . import jwt
#from flask_jwt_extended import jwt_required, get_jwt_identity

# from flask_jwt_extended import (
#     JWTManager, create_access_token, create_refresh_token, get_jti,
#     jwt_refresh_token_required, get_jwt_identity, jwt_required, get_raw_jwt
# )

from services import bcrypt
from models.client import Client

auth_blueprint = Blueprint('auth_api', __name__)
blacklist = set()

# Function to check if a token has been blacklisted.
@jwt.token_in_blacklist_loader
def check_if_token_in_blacklist(decrypted_token):
    jti = decrypted_token['jti']
    return jti in blacklist
"""
see https://flask-jwt-extended.readthedocs.io/en/stable/blacklist_and_token_revoking/
"""


#login route
@auth_blueprint.route('/login', methods=['POST'])
def login():
    print(f'Start login()')
    # To log user in and return an authentication token
    # Body: {email, password}
    # Return {auth_token}    
    body = request.json
    first_nam = request.json.get('username', None)

    to_check = Client.query.filter_by(email=body['email']).first()
    print(f'Client.query.filter_by(email passed!')
    print(body['password'])
    print(to_check.password)
    if bcrypt.check_password_hash(to_check.password, body['password']):
         # Create JWT token and return it
        print(f'bcrypt.check_password_hash(  passed!')     
        access_token = create_access_token(to_check.id)
        print(f'create_access_token(to_check.id) passed!')
        return{
            'message': 'Hey you logged in fine',
            'access_token'  :  access_token                   #This appears in Postman
        }
    else:
        return {
            'message': 'Incorrect password'
        }  

#logout route
@auth_blueprint.route('/logout', methods=['DELETE'])
@jwt_required
def logout():
    jti = get_raw_jwt()['jti']
    blacklist.add(jti)    
    return 'Logging out. Goodbye!'

"""
# Endpoint for revoking the current users access token
@app.route('/logout', methods=['DELETE'])
@jwt_required
def logout():
    jti = get_raw_jwt()['jti']
    blacklist.add(jti)
    return jsonify({"msg": "Successfully logged out"}), 200
"""


#register route
@auth_blueprint.route('/register', methods=['POST'])
def register():
    body = request.json
    message = create_client(     # create_client() defined in client_service.py
        body['email'], 
        bcrypt.generate_password_hash(body['password']).decode('utf-8'), 
        body['f_name'], 
        body['l_name'],
    )    
    return {
        'message': message
    }
