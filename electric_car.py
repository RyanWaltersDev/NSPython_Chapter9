# RyanWaltersDev Jul 20 2021 Learning about inheritance

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
        if miles < 0:
            print("Nice try! You can't roll back an odometer.")
        else:
            self.odometer_reading += miles

class ElectricCar(Car):
    '''Represents aspects of a car, specific to electric vehicles.'''

    def __init__(self, make, model, year):
        '''
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        '''
        super().__init__(make, model, year)
        self.battery_size = 75

    def describe_battery(self):
        '''Print a statement describing the battery size.'''
        print(f"This car has a {self.battery_size}-kwh battery.")

my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()

# END OF PROGRAM
