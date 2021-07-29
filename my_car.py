from car import Car

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
