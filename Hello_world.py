#print("hello world!")
#print("hello again")


#print(5+3)
#a string, and int, floating point number (i.e. float) = numbers with decimal points
#if one number in calc is a float then all numbers become float
# the comma separates arguments
#print is a function call, inside parentheses you can have multiple arguments
#functions are also called methods, is organised into a heirachy to make sure code processes in order.
print()
print("this is equal to", 5+3.0)
#interview question - order of opperations = moludo is % this prints out the remainder rather than the actual result. 
# this is important for coding, as the remained can be an important indicator of function success 
# parentheses, exponents, multiplication, division, addition, substraction - Please Excuse My Dear Aunt Sally
# below = 23*3 = 75, 75 modulo 4 = 3 (75/4 = 18.75, or 18 with 3 remainder), then 100-3 so output is 97
print(100 - 25 * 3 % 4)

# greater than or greater than or equal to is a question and provides a true/false answer
# to ask a true/false is X equal to y then you need to uses double = (i.e. ==)
# print("is 5 > -2 it greater", 5 > -2)
# print(5==3)
# print("is 5 equal to 3?", 5==3)
# not equal is called bang e.g. 5! is not equal to 3. != is an opperator, it is an opperation
# print(5!=3)

# HANDY SHORTCUT - 'command /' will turn lines into comments and back again.

## VARIABLES
# cars=100
# space_in_a_car = 4.0
# drivers = 30
# passengers = 90
# cars_not_driven = cars - drivers
# cars_driven = drivers
# carpool_capacity = cars_driven * space_in_a_car
# average_passengers_per_car = passengers / cars_driven

# print("cars available", cars)
# print("drivers available", drivers)
# print("empty cars today", cars_not_driven)
# print("carpool capacity", carpool_capacity)
# print("passengers today", passengers)
# print("average number of people in each car", average_passengers_per_car)

#a 'for' loop is an iterable, so it will print each item it encounters in the string one by one, so one on each line
string="some string"
for x in string:
    print(x)

string=["some string", "another string"]
for x in string:
    print(x)

