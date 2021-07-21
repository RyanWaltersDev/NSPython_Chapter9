# RyanWalters Dev Jul 11 2021 -- TIY 9-3

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

# Define instances
user1 = User('ryan', 'walters', 'milledgeville, georgia', '27')
user2 = User('brooke', 'yost', 'milledgeville, georgia', '23')
user3 = User('dixon', 'cassara', 'macon, georgia', '29')
user4 = User('grey', 'newell', 'smyrna, georgia', '28')

# Method calls
user1.greet_user()
user1.describe_user()

user2.greet_user()
user2.describe_user()

user3.greet_user()
user3.describe_user()

user4.greet_user()
user4.describe_user()

# New instance for TIY 9-5
user5 = User('colton', 'bragdon', 'decatur, georgia', '28')
user5.greet_user()
user5.describe_user()

user5.increment_login_attempts()
user5.increment_login_attempts()
print(f"{user5.first_name.title()} has attempted to log in "
    f"{user5.login_attempts} times.")
user5.reset_login_attempts()
print(f"{user5.first_name.title()} has attempted to log in "
    f"{user5.login_attempts} times.")

# END OF PROGRAM
        