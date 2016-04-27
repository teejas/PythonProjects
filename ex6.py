# Variable declaration for the string joke
x = "There are %d types of people in the world." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)
# Print joke
print x
print y
# Reiterate joke
print "I said: %r." % x
print "I also said: '%s'" % y 
# Joke isn't funny variables
hilarious = False
joke_evaluation = "Isn't this joke so funny?! %r" 
# Print joke evaluation
print joke_evaluation % hilarious
# Two part string
w = "This is the left side..."
h = " of a string with a right side"
# Print in one line
print w + h