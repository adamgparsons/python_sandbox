# If/ Else conditions are used to decide to do something based on something being true or false

x = 10
y = 10

# Simple if

# if x == y:
#     print(f'{x} is equal to {y}')

# if/else

# if x > y:
#     print(f'{x} is greater than {y}')
# else:
#     print(f'{x} is less than {y}')

# elif (else if)

# if x > y:
#     print(f'{x} is greater than {y}')
# elif x < y:
#     print(f'{x} is less than {y}')
# else:
#     print(f'{x} is equal to {y}')

# Nested if

# if x > 2:
#     if x < 20:
#         print('nested ifs')

# Logical operators (and, or, not) - Used to combine conditional statements
# if x > 2 and x < 20:
#     print('Logical and operator')


# if x > 2 or x < 20:
#     print('Logical or operator')


# Membership Operators (not, not in) - Membership operators are used to test if a sequence is presented in an object

# if not(x == y):
#     print(f'{x} does not equal {y}')

myList = [1, 2, 3, 4, 5]

# in
if 2 in myList:
    print('In the list')

# not in
if x not in myList:
    print('Not in the list')


# Identity Operators (is, is not) - Compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:

# is
if x is y:
    print(f'{x} is {y}')

# is not
if x is not y:
    print(f'{x} is not {y}')
