# homework assignment section 9-5
class User:
    """Modeling a user."""

    def __init__(self, first_name, last_name, id, user_name):
        """Initialize user attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.id = id
        self.user_name = user_name
        self.login_attempts = 1

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

user123 = User('tom', 'smith', '123', 'tsmith')
print(f"Login attempts: {user123.login_attempts}")
user123.increment_login_attempts()
print(f"Login attempts: {user123.login_attempts}")
user123.increment_login_attempts()
print(f"Login attempts: {user123.login_attempts}")
user123.reset_login_attempts()
print(f"Login attempts: {user123.login_attempts}")
