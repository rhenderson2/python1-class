# homework assignment section 9-3
class User:
    """Modeling a user."""

    def __init__(self, first_name, last_name, id, user_name):
        """Initialize user attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.id = id
        self.user_name = user_name

    def describe_user(self):
        """Simulate a user."""
        print(f"Full name: {self.first_name.title()} {self.last_name.title()}"
              f"\nUser name: {self.user_name}\nUser ID: {self.id}")

    def greet_user(self):
        """Welcoming a user."""
        print(f"Hello {self.first_name.title()} {self.last_name.title()},"
              f"\n\tWelcome!")

user123 = User('tom', 'smith', '123', 'tsmith')
user123.describe_user()
user123.greet_user()
print('\n')
user321 = User('phil', 'jones', '321', 'pjones')
user321.describe_user()
user321.greet_user()
print('\n')
user132 = User('mary', 'jones', '132', 'mjones')
user132.describe_user()
user132.greet_user()

