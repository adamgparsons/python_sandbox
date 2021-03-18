# A class is like a blueprint for creating objects. An object has properties and methods(functions) associated with it. Almost everything in Python is an object

# Create class
class User:
    # Constructor
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age

    def greeting(self):
        return f'My name is {self.name} and I am {self.age}'

    def has_birthday(self):
        self.age += 1


class Customer(User):
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
        self.balance = 0

    def set_balance(self, balance):
        self.balance = balance

    def greeting(self):
        return f'My name is {self.name} and I am {self.age} and I owe a balance of {self.balance}'


# Init user object
adam = User('Adam', 'adam@email.com', '32')
john = User('John', 'john@email.com', '25')

# edit property
adam.age = 32

# Call method
# print(adam.has_birthday())

# print(adam.age)

# Init customer
jane = Customer('jane', 'jane@email.com', 54)
jane.set_balance(500)

print(jane.greeting())
