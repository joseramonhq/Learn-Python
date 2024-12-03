# Exercises: Level 1
# Inside 30DaysOfPython create a folder called day_2. Inside this folder create a file named variables.py
# Write a python comment saying 'Day 2: 30 Days of python programming'
# Declare a first name variable and assign a value to it
import math


name = 'jose'
# Declare a last name variable and assign a value to it
lastname = 'ramon'
# Declare a full name variable and assign a value to it
fullname = name + lastname 
# Declare a country variable and assign a value to it
country = 'Spain'
# Declare a city variable and assign a value to it
city = 'Santander'
# Declare an age variable and assign a value to it
age = 50
# Declare a year variable and assign a value to it
year = 1974
# Declare a variable is_married and assign a value to it
is_married = False
# Declare a variable is_true and assign a value to it
is_true = is_married
# Declare a variable is_light_on and assign a value to it
is_light_on = False
# Declare multiple variable on one line
surname, dog_name, cat_name = 'Hidalgo', 'Kun', 'Snif'
# Exercises: Level 2
# Check the data type of all your variables using type() built-in function
print(type(name))
print(type(lastname))
print(type(fullname))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))
print(type(surname))
print(type(dog_name))
print(type(cat_name))


# Using the len() built-in function, find the length of your first name
print(len(name))
# Compare the length of your first name and your last name
print(len(name)==len(lastname))
# Declare 5 as num_one and 4 as num_two
num_one = 5
num_two = 4
# Add num_one and num_two and assign the value to a variable total
total = num_one + num_two
# Subtract num_two from num_one and assign the value to a variable diff
diff = num_one - num_two
# Multiply num_two and num_one and assign the value to a variable product
product = num_two * num_one
# Divide num_one by num_two and assign the value to a variable division
division = num_one / num_two
# Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
remainder = num_two % num_one
# Calculate num_one to the power of num_two and assign the value to a variable exp
exp = num_one ** num_two
# Find floor division of num_one by num_two and assign the value to a variable floor_division
floor_division = num_one // num_two
# The radius of a circle is 30 meters.
# Calculate the area of a circle and assign the value to a variable name of area_of_circle
area_of_circle = math.pi * 30 ** 2
print(area_of_circle)
# Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
circum_of_circle = 2 * math.pi * 30 * 2
print(circum_of_circle)
# Take radius as user input and calculate the area.

radius = input('Input radius')
area_of_circle = math.pi * float(radius) ** 2
print(area_of_circle)

# Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names
name = input("name")
lastname = input("lastname")
country =input("country")
age =input("age")
print(name, lastname,country,age)

# Run help('keywords') in Python shell or in your file to check for the Python reserved words or keywords

help(len)
help(type)