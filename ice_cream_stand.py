from restaurant import Restaurant
'''Modeling an ice cream stand'''

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

# Ice cream stand instance and method calls.
ice_cream_stand = IceCreamStand("Bubba's Ice Cream", "Ice Cream Stand", )
ice_cream_stand.describe_restaurant()
ice_cream_stand.open_restaurant()
ice_cream_stand.display_flavors(['Chocolate', 'Vanilla', 'Strawberry'])

# END OF PROGRAM
