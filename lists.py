# A List is a collection which is ordered and changeable. Allows duplicate members.
# A list is basically an array

# Create list
# numbers = [1, 2, 3, 4, 5]
fruits = ['apple', 'pineapple', 'orange', 'grapes', 'pear']

# Creating a list using a constructor
# numbers = list((1, 2, 3, 4, 5))

# Get a value from a list
# print(fruits[1])

# Gets number of items in a list
# print(len(fruits))

# Append to list
fruits.append("mangoes")

# Remove from list
fruits.remove('grapes')

# Insert into a position in list
fruits.insert(2, 'banana')

# Remove from position
fruits.pop(3)

# Reverse list
fruits.reverse()

# Sorting a lits
fruits.sort()

# Reverse sort
fruits.sort(reverse=True)

print(fruits)
