'''A module to model basic facts about a restaurant'''

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

# END OF PROGRAM
