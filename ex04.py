cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")

# What do you mean by “read the ﬁ le backward”?
#Very simple. Imagine you have a ﬁ le with 16 lines of code in it. Start at line 16, and compare it to
# my ﬁle at line 16. Then do it again for 15, and so on, until you’ve read the whole ﬁ le backward.

#Why does / (divide) round down?
#It’s not really rounding down; it’s just dropping the fractional part after the decimal. Try doing
#7.0 / 4.0 and compare it to 7 / 4 and you’ll see the difference.