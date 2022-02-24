# number of cars
cars = 100

# number of people can fit into a car
space_in_a_car = 4.0

# number of drivers
drivers = 30

# number of passengers
passengers = 90

# number of cars without drivers
cars_not_driven = cars - drivers

# number of cars with drivers
cars_driven = drivers

# number of people can fit into all cars
carpool_capacity = cars_driven * space_in_a_car

# average number of passengers in each car
average_passengers_per_car = passengers / cars_driven

print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")
