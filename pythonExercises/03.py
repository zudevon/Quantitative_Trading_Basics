"""
Write a script that extracts numbers from a string.
The string may have more than one set of numbers in it.
Example: ‘abc45 def 53xyz’ would be represented as a list of [45,53].

"""
import re
strings = ['abc4 def 53xyz', 'abc45 def 3xyz', 'abc45 def 53xyz', 'abc45 def 53xyz']


def new_interger_list(some_string):
    return [int(s) for s in re.findall(r'\d+', some_string)]


numbers = []
for i in strings:
    numbers.append(new_interger_list(i))

print(numbers)
