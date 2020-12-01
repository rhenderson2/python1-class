# File for Privileges and Admin classes for hw_9-12
from user_class import User
class Privileges:
    """Creating Privileges as its own class"""

    def __init__(self, privileges=['can add post', 'can delete post', 'can ban user']):
        """Initialize privileges attribute."""
        self.privileges = privileges

    def show_privileges(self):
        print(self.privileges)


class Admin(User):
    def __init__(self, first_name, last_name, id, user_name):
        super().__init__(first_name, last_name, id, user_name)
        self.privileges = Privileges()
