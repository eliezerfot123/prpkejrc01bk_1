from qaroni.database import db
from sqlalchemy.orm import Session
from apps.user.models import User
from werkzeug.security import generate_password_hash, check_password_hash
from qaroni.mail import send_mail
from qaroni.extensions import bcrypt


class CreateUserDAO:
    def __init__(self) -> None:
        self.db = db
        self.session = Session(self.db.engine)
        self.model = User

    def create(self, email: str, password: str, first_name: str, last_name: str, type: str) -> User:
        """Create a new user."""
        # validate data no exists
        if self.validate_user(email):
            return None
        hash_password = generate_password_hash(password)
        user = self.model(email=email, first_name=first_name, last_name=last_name, role=type, password=hash_password)

        # save user
        self.session.add(user)
        self.session.commit()
        # send email
        #send_mail(email, "Welcome", f"Welcome {user.email} to Qaroni.")
        return user
    

    def validate_user(self, email: str) -> bool:
        user = self.model.query.filter_by(email=email).first()
        if user:
            return True
        return False