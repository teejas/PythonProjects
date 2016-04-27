# Declaring variables for a carpool event.
# Remember all necessary components:
cars = 100
space_in_a_car = 4.0 
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven
# Now some statements using the variables
print "There are", cars, "cars available"
print "There are only", drivers, "drivers available"
print "There will be", cars_not_driven, "cars not driven today"
print "We can transport", carpool_capacity, "people today"
print "We have", passengers, "people to transport today"
print "We need to put", average_passengers_per_car, "people in each car"
print "Each car can carry", space_in_a_car, "people"