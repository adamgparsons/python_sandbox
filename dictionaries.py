# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
# Often decode JSON into dictionaries

# Simple dict
person = {
    'first_name': 'Adam',
    'last_name': 'Parsons',
    'age': 32
}

# Simple dict using a constructor
# person = dict(first_name='Adam', last_name='Parsons', age=32)

# Access a single value
# print(person['first_name'])

# Access a single value using get method
# print(person.get('first_name'))

# Add a key/value pair
person['phone'] = '123-123-123'

# Get keys
# print(person.keys())

# Get items
# print(person.items())

# Make a copy
person2 = person.copy()
person2['first_name'] = "Hello   "

# Remove an item
# del person['age']

# Remove an item using pop
person.pop('phone')

# List of dict - similiar to an array of objects in JS
people = [{"first_name": 'Bob', "age": 25},
          {"first_name": 'Samantha', "age": 56}]

# Get specific property
print(people[1]['first_name'])

# print(people)
