# -*- coding: utf-8 -*-
"""User models."""
import datetime as dt

from flask_login import UserMixin
from sqlalchemy.ext.hybrid import hybrid_property
from werkzeug.security import check_password_hash, generate_password_hash

from qaroni.database import BaseModel, Column, db, reference_col, relationship
from qaroni.extensions import bcrypt


class User(UserMixin, BaseModel):
    """A user of the app."""

    __tablename__ = "users"

    email = Column(db.String(80), unique=True, nullable=False)
    _password = Column("password", db.String(256))
    first_name = Column(db.String(30), nullable=True)
    last_name = Column(db.String(30), nullable=True)
    role = Column(db.String(10), nullable=True)
    active = Column(db.Boolean(), default=True)
    is_admin = Column(db.Boolean(), default=False)

    @hybrid_property
    def password(self):
        """Hashed password."""
        return self._password

    @password.setter
    def password(self, value):
        """Set password."""
        self._password = bcrypt.generate_password_hash(value)

    def set_password(self, secret):
        self._password = generate_password_hash(secret)

    def check_password(self, value):
        """Check password."""
        return bcrypt.check_password_hash(self._password, value)

    @property
    def full_name(self):
        """Full user name."""
        return f"{self.first_name} {self.last_name}"

    def __repr__(self):
        """Represent instance as a unique string."""
        return f"<User({self.email!r})>"
