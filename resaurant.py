# RyanWaltersDev Jul 11 2021 -- TIY 9-1 and 9-4

class Restaurant:
    '''A simple model of a restaurant'''

    def __init__(self, restaurant_name, cuisine_type, number_served=0):
        '''Initialize name and cuisine type attributes'''
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = number_served

    def describe_restaurant(self):
        '''Print restaurant name and cuisine type'''
        print(f"{self.restaurant_name} is a {self.cuisine_type} style "
            "restaurant.")

    def open_restaurant(self):
        '''Print a message to indicate restaurant opening'''
        if self.number_served == 0:
            print(f"{self.restaurant_name} is open!")
        else:
            print(f"{self.restaurant_name} is open!")
            print(f"So far we have served {self.number_served} customers.")

    def set_number_served(self, customers_served):
        self.number_served = customers_served

    def increment_number_served(self, customers_served):
        self.number_served += customers_served

class IceCreamStand(Restaurant):
    '''Model a small ice cream stand'''

    def __init__(self, restaurant_name, cuisine_type, flavors=None, 
                number_served=0):
        super().__init__(restaurant_name, cuisine_type, number_served)
        self.flavors = flavors

    def display_flavors(self, flavors):
        '''Print a current list of flavors'''
        print("Below is a list of our available flavors:")
        print(", " .join(flavors))

# Define instances
med_restaurant = Restaurant('Metropolis Cafe', 'Mediterranean')
mex_restaurant = Restaurant('Bollywood Tacos', 'Mexican/Indian Fusion')
sushi_restaurant = Restaurant('Kai Thai', 'Japanese/Thai')
new_restaurant = Restaurant('Popadopolis', 'Surf & Turf', 0)


# Call methods
med_restaurant.describe_restaurant()
med_restaurant.open_restaurant()

mex_restaurant.describe_restaurant()
mex_restaurant.open_restaurant()

sushi_restaurant.describe_restaurant()
sushi_restaurant.open_restaurant()

# TIY 9-4 - Initial print
new_restaurant.describe_restaurant()
new_restaurant.open_restaurant()

# Set number served with dot notation and reprint
new_restaurant.number_served = 15
new_restaurant.open_restaurant()

# Set number served by calling method and reprint
new_restaurant.set_number_served(30)
new_restaurant.open_restaurant()

# Increment number served by calling method and reprint
new_restaurant.increment_number_served(67)
new_restaurant.open_restaurant()
new_restaurant.increment_number_served(450)
new_restaurant.open_restaurant()

# Ice cream stand instance and method calls.
ice_cream_stand = IceCreamStand("Bubba's Ice Cream", "Ice Cream Stand", )
ice_cream_stand.describe_restaurant()
ice_cream_stand.open_restaurant()
ice_cream_stand.display_flavors(['Chocolate', 'Vanilla', 'Strawberry'])

# END OF PROGRAM
