from user_module import User 
from admin_module import Privileges, Admin
'''Modeling a simple admin profile'''

admin = Admin('ryan', 'walters', 'macon, georgia', 27)
admin.greet_user()
admin.privileges.show_privileges(['can delete system 32'])

# END OF PROGRAM
