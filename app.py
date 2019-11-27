from flask import Flask
from models import db
from services import bcrypt
from controllers import jwt, auth_blueprint, event_blueprint
#from services.client_service import create_client

from flask_jwt_extended import (
    JWTManager, create_access_token, create_refresh_token, get_jti,
    jwt_refresh_token_required, get_jwt_identity, jwt_required, get_raw_jwt
)


app = Flask(__name__)

#app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv('DATABASE_URL')  # in config.py
app.config.from_object('config.Development') 

# Setup the flask-jwt-extended extension. See:

# Setup our redis connection for storing the blacklisted tokens
# revoked_store = redis.StrictRedis(host='localhost', port=6379, db=0,
#                                   decode_responses=True)

db.init_app(app)
bcrypt.init_app(app)
jwt.init_app(app)

# Add blueprints here
app.register_blueprint(auth_blueprint, url_prefix="/auth")
app.register_blueprint(event_blueprint, url_prefix="/event")

if __name__ == "__main__":
    app.run()