from qaroni.database import db
from sqlalchemy.orm import Session
from flask import make_response
from apps.user.models import User
from werkzeug.security import generate_password_hash, check_password_hash
from qaroni.extensions import bcrypt

class LoginUserDAO:
    def __init__(self) -> None:
        self.db = db
        self.session = Session(self.db.engine)
        self.model = User

    def login_user(self, request_data):
        """
        Log in user with provided data.
        """
        email = request_data["email"]
        password = request_data["password"]

        # check if user exists and password is correct
        user = self.model.query.filter_by(email=email).first()
        import ipdb; ipdb.set_trace()
        if not user:
            # returns 401 if user does not exist
            return False
        # validate with check_password_hash method
        #if check_password_hash(user.password, password):
        #    return user
        elif user != None:
            return user
