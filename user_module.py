'''A module for basic facts and priviliges for a user'''

class User:
    '''Model a user and their basic info'''

    def __init__(self, first_name, last_name, location, age, login_attempts=0):
        '''Initialize attributes for user'''
        self.first_name = first_name
        self.last_name = last_name
        self.location = location
        self.age = age
        self.login_attempts = login_attempts

    def describe_user(self):
        '''Print user information'''
        print("Here are some basic facts that you provided.")
        print(f"First Name: {self.first_name.title()}")
        print(f"Last Name: {self.last_name.title()}")
        print(f"Location: {self.location.title()}")
        print(f"Age: {self.age}")

    def greet_user(self):
        '''A simple greeting'''
        print(f"\nHello, {self.first_name.title()}!")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

# END OF PROGRAM
