# homework assignment section 9-12
from user_class import User
from privileges_admin import Privileges, Admin

new_admin1 = Admin('paul', 'mohn', 394, 'pmohn')

new_admin1.describe_user()

new_admin1.privileges.show_privileges()
