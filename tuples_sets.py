# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# A tuple is unchangeable!!!

# Simple tuple
fruit_tuple = ('Apple', 'Orange', 'Mango')

# Using a contructor to create a tuple
# fruit_tuple = tuple(('Apple', 'Orange', 'Mango'))

# Get a single value
# print(fruit_tuple[1])

# Tuples with one value should have a trailing comma
fruit_tuple_2 = ('Apple',)

# Getting length of tuple
# print(len(fruit_tuple))

# You can't delete individual items
# But you can delete the whole tuple
del fruit_tuple_2


# print(fruit_tuple)

# A Set is a collection which is unordered and unindexed. No duplicate members.
# It ignores duplicate items

fruit_set = {'Apple', 'Orange', 'Mango'}

# Check if in set
# print('Apple' in fruit_set)

# Add to a set
fruit_set.add("Banana")

# Remove an item from a set
fruit_set.remove("Mango")

# Clear a set
fruit_set.clear()

# Delete a set
# del fruit_set


print(fruit_set)
