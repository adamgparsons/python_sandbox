# A function is a block of code which only runs when it is called. In Python, we do not use parentheses and curly brackets, we use indentation with tabs or spaces

# Create a function
# def sayHello(name):
# '''
# Prints Hello and then name
# '''
#   print('Hello ' + name)

# sayHello('Adam')

# If you want to pass in a default value


# def sayHello(name='John'):
#     '''
#     Prints Hello and then name
#     '''
#     print('Hello ' + name)


# sayHello()

# Return a value
def getSum(num1, num2):
    '''
    Returns sum of 2 numbers
    '''
    total = num1 + num2
    return total


# print(getSum(1, 2))

def addOnetoNum(num):
    num += 1
    return num


# print(addOnetoNum(1))


# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression. Very similar to JS arrow functions
# Commonly one line

def newGetSum(num1, num2): return num1 + num2


print(newGetSum(1, 2))


def newAddOnetoNum(num1): return num1 + 1


print(newAddOnetoNum(1))
