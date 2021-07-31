'''A set of classes that can be used to represent electric cars'''

from car import Car

class Battery:
    '''A simple attempt to model a battery for an electric car.'''

    def __init__(self, battery_size=75):
        '''Initialize the battery's attributes.'''
        self.battery_size = battery_size

    def describe_battery(self):
        '''Print a statement describing the battery size.'''
        print(f"This car has a {self.battery_size}-kwh battery.")\

    def get_range(self):
        '''Print a statement about the range this battery provides'''
        if self.battery_size == 75:
            range = 260
            print(f"This car can go about {range} miles on a full charge.")
        elif self.battery_size == 100:
            range = 315
            print(f"This car can go about {range} miles on a full charge.")
        else:
            print(f"The battery size that you have entered is not valid.")

    def upgrade_battery(self):
        '''Check battery size and set capacity to 100'''
        if self.battery_size != 100:
            self.battery_size = 100


class ElectricCar(Car):
    '''Represents aspects of a car, specific to electric vehicles.'''

    def __init__(self, make, model, year):
        '''
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        '''
        super().__init__(make, model, year)
        self.battery = Battery()

    def fill_gas_tank(self):
        '''Electric cars don't have gas tanks.'''
        print(f"This car does not need a gas tank!")

# END OF PROGRAM
