from qaroni.database import db
from sqlalchemy.orm import Session
from apps.user.models import User
from werkzeug.security import generate_password_hash, check_password_hash
from qaroni.mail import send_mail

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
        user = self.model(email=email, first_name=first_name, last_name=last_name, role=type)
        user.password = generate_password_hash(password)  # hash password
        user.save(commit=True)

        # send email
        send_mail(email, "Welcome", f"Welcome {user.email} to Qaroni.")
        return user
    

    def validate_user(self, email: str) -> bool:
        user = self.model.query.filter_by(email=email).first()
        if user:
            return True
        return False