# RyanWaltersDev Jul 11 2021 -- TIY 9-1

class Restaurant:
    '''A simple model of a restaurant'''

    def __init__(self, restaurant_name, cuisine_type):
        '''Initialize name and cuisine type attributes'''
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        '''Print restaurant name and cuisine type'''
        print(f"{self.restaurant_name} is a {self.cuisine_type} style "
            "restaurant.")

    def open_restaurant(self):
        '''Print a message to indicate restaurant opening'''
        print(f"{self.restaurant_name} is now open!")

# Define instances
med_restaurant = Restaurant('Metropolis Cafe', 'Mediterranean')
mex_restaurant = Restaurant('Bollywood Tacos', 'Mexican/Indian Fusion')
sushi_restaurant = Restaurant('Kai Thai', 'Japanese/Thai')


# Call methods
med_restaurant.describe_restaurant()
med_restaurant.open_restaurant()

mex_restaurant.describe_restaurant()
mex_restaurant.open_restaurant()

sushi_restaurant.describe_restaurant()
sushi_restaurant.open_restaurant()

# END OF PROGRAM
