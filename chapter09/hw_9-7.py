# homework assignment section 9-7
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


class Admin(User):
    def __init__(self, first_name, last_name, id, user_name):
        super().__init__(first_name, last_name, id, user_name)
        self.privileges = ['can add post', 'can delete post', 'can ban user']

    def show_privileges(self):
        print(self.privileges)

my_admin = Admin('Rick', 'Henderson', 344, 'rhenderson')

my_admin.show_privileges()

