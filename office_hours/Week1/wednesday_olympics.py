x = '5'
y = 8
# print(x + y) # Results in TypeError

# Truthy and falsy statements

# All of these are equivalent in Python
# 0 and False are the same
# 1 and True are the same
# None is unique - in an "if" statement, something that is None will go to False effectively
# if not None:
#     print("Not None")

z = "10"
if z == 10: # Must be exact in terms of value AND type
    print(z)