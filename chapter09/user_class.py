# File for User class for hw_9-12
class User:
    """Modeling a user."""

    def __init__(self, first_name, last_name, id, user_name):
        """Initialize user attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.id = id
        self.user_name = user_name
        self.login_attempts = 1

    def describe_user(self):
        """Simulate a user."""
        print(f"Full name: {self.first_name.title()} {self.last_name.title()}"
              f"\nUser name: {self.user_name}\nUser ID: {self.id}")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0
