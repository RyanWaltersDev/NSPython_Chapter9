from restaurant import Restaurant
'''Modeling a local Italian Restaurant'''

class Italian_Restaurant(Restaurant):
    '''Italian Restaurant model'''

    def __init__(self, restaurant_name, cuisine_type, sauce_types=None, 
        pasta_types=None, number_served=0):
        '''Initializing attributes for restaurant'''
        super().__init__(restaurant_name, cuisine_type, number_served)
        self.sauce_types = sauce_types
        self.pasta_types = pasta_types

    def display_pasta(self, pasta_types):
        '''Print list of pasta types and'''
        print("Here is a list of our different pasta types:")
        pasta_types = [pasta.capitalize() for pasta in pasta_types]
        print(f", " .join(pasta_types[0:-1]) +", and "+pasta_types[-1])

    def display_sauces(self, sauce_types):
        '''Print list of sauces'''
        print("Here is a lsit of our different sauce types:")
        sauce_types = [sauce.capitalize() for sauce in sauce_types]
        print(f", " .join(sauce_types[0:-1]) +", and "+sauce_types[-1])


joannas = Italian_Restaurant("joanna's", 'italian')
joannas.display_pasta(['fettucini', 'linguini', 'penne'])
joannas.display_sauces(['alfredo', 'marinara', 'pesto'])