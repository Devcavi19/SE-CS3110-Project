"""Models module for the application."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    """User model for storing user details."""
    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(50), nullable=False)
    lname = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(256), nullable=False)

    def __repr__(self):
        """Return string representation of the user."""
        return f'<User {self.fname} {self.lname}>'

    def get_full_name(self):
        """Return user's full name."""
        return f"{self.fname} {self.lname}"

    def to_dict(self):
        """Convert user object to dictionary."""
        return {
            'id': self.id,
            'fname': self.fname,
            'lname': self.lname,
            'email': self.email
        }
