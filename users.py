# RyanWalters Dev Jul 11 2021 -- TIY 9-3

class User:
    '''Model a user and their basic info'''

    def __init__(self, first_name, last_name, location, age):
        '''Initialize attributes for user'''
        self.first_name = first_name
        self.last_name = last_name
        self.location = location
        self.age = age

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

# END OF PROGRAM
        