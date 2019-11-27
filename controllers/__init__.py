"""## Controllers:: __init__.py ###"""

from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity
)

jwt = JWTManager()
blacklist = set()

from .auth_controller import auth_blueprint
from .event_controller import event_blueprint
