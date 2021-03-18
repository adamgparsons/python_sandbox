# A module is basically a file containing a set of functions to include in your application. There are core python modules, modules you can install using the pip package manager (including Django) as well as custom modules

# Core modules
# import datetime

# or if you want a specific part of a module

import camelcase
from time import time
from datetime import date


# Custom modules
import validator
from validator import validate_email
# today = datetime.date.today()
today = date.today()

# print(today)

timestamp = time()

# print(timestamp)

# pip modules

camel = camelcase.CamelCase()
text = "hello there world"
print(camel.hump(text))

email = "test@test.com"

print(validate_email(email))
