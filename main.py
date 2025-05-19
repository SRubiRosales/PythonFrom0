# This is a comment
"""
This is a comment
with multiple
line breaks
"""
print("Hello world!, from script in Python")

name = "Código Facilito" # Str
print(name)
print(type(name))

# Strings (" - ')
first_name = "Sharon"
last_name = 'Rosales'
print(first_name)
print(last_name)
print(type(first_name))

# Integers +-
age = 20 # int
number = 100_000_000
print(type(age))
print(number)

a = 10
result = a + 10
print("Result is: ", result)
print(result//10)

# Floats +-
pi = 3.1416
print(type(pi))
print(result/10)

# Booleans (True | False)
is_active = True
print(is_active)
print(type(is_active))

VERSION = 3.13
print(VERSION)

# Relational operators
number_one = 10
number_two = 20.0
compare = number_one == number_two
print(compare)
print(type(compare))
print(number_one < number_two)

# Logic operators
print(True and True) # True
print(True and True and number_one == number_two) # False
print(True and True and number_one != number_two) # True
print(True 
      and True 
      and number_one != number_two 
      and number_one < 100 
      and number_two > 200) # False
print(True or True) # True
print(False 
      and False 
      and number_one == number_two 
      and number_one < 100 
      and number_two > 200) # True
print(not True) # False
print(not False) # True
print(not not True) # True
print(not not not True) # False
compare = not(
    (number_one == number_two and True)
    and (number_one < 100)
    and (number_two < 100)
    or (number_one > 100 and number_two > 200)
)
print(compare) # True

message = input("Input your name: ") # Str
print("Hello, ", message)

first_name = input("Name: ")
age = int(input("Age: "))
height = float(input("Height: "))
status = input("Is your user active? (y/n) ") == "y"
print(first_name)
print(age)
print(height)
print(status)