# Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods

name = 'Adam'
age = 32

# Concatenate
# print('Hello I am ' + name + ' and I am ' + str(age))

# String Formatting

# Arguments by position

# print('{}, {}, {}'.format('a', 'b', 'c'))
# print('{1}, {2}, {0}'.format('a', 'b', 'c'))

# Arguments by name
# print('My name is {name} and I am {age}'.format(name=name, age=age))


# F-Strings (only in 3.6+) similiar to template strings in JS
# print(f'My name is {name} and I am {age}')

# String Methods
s = 'Hello there World'

# Capitalise first letter
# print(s.capitalize())

# Make all upper
# print(s.upper())

# Make all lower
# print(s.lower())

# Swap case
# print(s.swapcase())

# Get length of string
# print(len(s))

# Replace
# print(s.replace('World', 'everyone'))

# Count
sub = "H"
print(s.count(sub))
