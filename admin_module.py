from user_module import User 

class Privileges:
    '''Model list of privileges for Admin'''

    def __init__(self, privileges=0):
        '''Initialize attribute for privileges'''
        self.privileges = privileges

    def show_privileges(self, privileges):
        '''Show a list of privileges for the admin'''
        print("Welcome Admin! Here is your current list of privileges:")
        print(", " .join(privileges))

class Admin(User):
    '''Model a special class for Administrators'''

    def __init__(self, first_name, last_name, location, age, login_attempts=0):
        '''Initalize attributes for admin'''
        super().__init__(first_name, last_name, location, age, login_attempts)
        self.privileges = Privileges()

# END OF PROGRAM
