# RyanWaltersDev Jul 13 2021 -- The car class

class Car:
    '''A simple attempt to represent a car.'''

    def __init__(self, make, model, year):
        '''Initialize attributes to describe a car.'''
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        '''Return a neatly formatted descriptive name.'''
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        '''Print a statement showing the car's mileage.'''
        print(f"This car has {self.odometer_reading} miles on it!")

    def update_odometer(self, milelage):
        '''
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        '''
        if milelage >= self.odometer_reading:
            self.odometer_reading = milelage
        else:
            print("Nice try! You can't roll back an odometer.")

    def increment_odometer(self, miles):
        '''Add the given amoutn to the odometer reading'''
        self.odometer_reading += miles

# First Car

my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 23
my_new_car.read_odometer()

my_new_car.update_odometer(33)
my_new_car.read_odometer()

# Second Car

my_used_car = Car('lexus', 'crv', 2011)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(120_550)
my_used_car.read_odometer()

my_used_car.increment_odometer(5_000)
my_used_car.read_odometer()

# END OF PROGRAM
