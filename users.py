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
        