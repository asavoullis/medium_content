import math

# basic example
name = "Tom"
message = f"Hello, {name}!"
print(message) # outputs: Hello, Tom!


### Embedding Expressions ###
# Variables
radius = 7.5
area_formula = math.pi * radius ** 2

# Using an f-string to incorporate a Python expression and formatting the result
# rounded to two decimal
area = f"The area of the circle is {area_formula:.2f} square units."
print(area, "\n")


### Function Calls Within Strings ###

# Define a function to greet a user
def greet(name):
    return "Hello, " + name

user_name = "Bob"


# Calling the greet function inside an f-string
greeting = f"{greet(user_name)}"
print(greeting, "\n")


### Direct Access to Data Structures ###
# Data dictionary
data = {'user': 'Carol', 'age': 34}

# Accessing dictionary elements directly in an f-string
info = f"{data['user']} is {data['age']} years old."
print(info, "\n")


