# Putting two strings together
x = "First string"
y = "Second string"

print(x + " " + y) # Correct
print(x + y) # Incorrect

print(x, y) # Correct

print("x" + "y") # Incorrect

# F-string demo
z = 50
print(f'The value of z is {z}')

print(f"{x} {y}") # Third way of putting strings together with an F-string

# print("The value of z is {}".format(z)) # Also works (older version of F-string)