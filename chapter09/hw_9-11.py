# homework assignment section 9-11
import import_user_admin_privilege as iuap


new_admin = iuap.Admin('fred', 'mann', 374, 'fmann')

new_admin.describe_user()

new_admin.privileges.show_privileges()
