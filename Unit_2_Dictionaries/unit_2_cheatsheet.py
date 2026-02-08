# Python Quick Reference Guide - CodePath TIP102 Unit 2

# ============= TYPE CASTING =============

# int() - Cast to integer
x = int(2.5)  # x will be 2 (floats round down)
y = int("5")  # y will be 5

# float() - Cast to float
x = float(2)  # x will be 2.0
y = float("5")  # y will be 5.0
z = float("5.3")  # z will be 5.3

# str() - Cast to string
x = str(2)  # x will be "2"
y = str(2.0)  # y will be "2.0"
z = str([1, 2, 3, 4])  # z will be "[1, 2, 3, 4]"


# ============= INFINITY =============

positive_infinity = float("inf")
negative_infinity = float("-inf")

# Finding minimum value example
lst = [5, 4, 3, 2, 1]


def get_min(lst):
    minimum = float("inf")
    for num in lst:
        if num < minimum:
            minimum = num
    return minimum


# Safe divide example
def safe_divide(a, b):
    if b == 0:
        if a > 0:
            return float("inf")
        else:
            return float("-inf")
    return a / b


# ============= ROUND FUNCTION =============

# Round to hundredth
x = 3.14159
rounded = round(x, 2)
print(rounded)  # Prints 3.14

# Round to nearest whole number
x = 3.14159
rounded = round(x)
print(rounded)  # Prints 3


# ============= ABSOLUTE VALUE =============

absolute_value = abs(5)  # Prints 5
absolute_value = abs(-5)  # Prints 5
absolute_value = abs(-3.14)  # 3.14


# ============= ENUMERATE =============

my_string = "code"
for index, char in enumerate(my_string):
    print(index, char)
# Prints:
# 0 c
# 1 o
# 2 d
# 3 e

cereals = ["cheerios", "fruity pebbles", "cocoa puffs"]
for count, cereal in enumerate(cereals, start=1):
    print(count, cereal)
# Prints:
# 1 cheerios
# 2 fruity pebbles
# 3 cocoa puffs


# ============= ZIP =============

names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
zipped = zip(names, ages)
print(list(zipped))  # Prints [('Alice', 25), ('Bob', 30), ('Charlie', 35)]

names = ["Alice", "Bob", "Charlie", "David"]
ages = [25, 30, 35]
zipped = zip(names, ages)
print(list(zipped))  # Prints [('Alice', 25), ('Bob', 30), ('Charlie', 35)]


# ============= DICTIONARY METHODS =============

# Setting and Updating Values
d = {"a": 1, "b": 2, "c": 3}
d["d"] = 4  # Adds new key-value pair
print(d)  # Outputs: {'a': 1, 'b': 2, 'c': 3, 'd': 4}
d["a"] = 100  # Updates existing key
print(d)  # Outputs: {'a': 100, 'b': 2, 'c': 3, 'd': 4}

# Accessing Elements - Direct Access
d = {"a": 1, "b": 2, "c": 3}
print(d["a"])  # Outputs: 1
print(d["b"])  # Outputs: 2

# Accessing Elements - get() method (safer)
d = {"a": 1, "b": 2, "c": 3}
print(d.get("a"))  # Outputs: 1
print(d.get("z"))  # Outputs: None
print(d.get("z", "Not Found"))  # Outputs: 'Not Found'

# Pop Method - Remove and return value
d = {"a": 1, "b": 2, "c": 3, "d": 4}
d.pop("a")  # Returns 1
print(d)  # Prints {'b': 2, 'c': 3, 'd': 4}
# d.pop('e')  # Raises KeyError

d = {"a": 1, "b": 2, "c": 3, "d": 4}
d.pop("a", None)  # Returns 1
print(d)  # Prints {'b': 2, 'c': 3, 'd': 4}
d.pop("e", None)  # Returns None
print(d)  # Prints {'b': 2, 'c': 3, 'd': 4}

# Keys Method - Get all keys
d = {"a": 1, "b": 2, "c": 3, "d": 4}
keys = d.keys()
print(keys)  # Prints ['a', 'b', 'c', 'd']

# Values Method - Get all values
d = {"a": 1, "b": 2, "c": 3, "d": 4}
values = d.values()
print(values)  # Prints [1, 2, 3, 4]

# Items Method - Get key-value pairs as tuples
d = {"a": 1, "b": 2, "c": 3, "d": 4}
items = d.items()
print(items)  # Prints [('a', 1), ('b', 2), ('c', 3), ('d', 4)]


# ============= NESTED DATA STRUCTURES =============

# Nested Lists
singers = ["Sabrina Carpenter", "FKA Twigs", "Elliot Smith"]

albums = [
    ["Sabrina Carpenter", "Short n' Sweet"],
    ["FKA Twigs", "Magdalene"],
    ["Elliot Smith", "Either/Or"],
]

numbers = [[1], [1, 2], [1, 2, 3]]

water_levels = ["Shallow", ["Deep", ["Deeper"]]]

# Matrix
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Accessing nested lists
albums = [
    ["Sabrina Carpenter", "Short n' Sweet"],
    ["FKA Twigs", "Magdalene"],
    ["Elliot Smith", "Either/Or"],
]
first_album = albums[0]
print(first_album)  # Output: ["Sabrina Carpenter", "Short n' Sweet"]

fka_twigs = albums[1][0]
print(fka_twigs)  # Output: FKA Twigs

# Updating nested lists
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix[2] = [100, 200, 300]
print(matrix)  # Output: [[1, 2, 3], [4, 5, 6], [100, 200, 300]]

matrix[1][1] = "Surprise!"
print(matrix)  # Output: [[1, 2, 3], [4, 'Suprise!', 6], [7, 8, 9]]

# Nested Dictionaries
address_book = {
    "John Doe": {
        "phone": "555-1234",
        "email": "johndoe@example.com",
        "address": {
            "street": "123 Maple Street",
            "city": "Springfield",
            "state": "IL",
            "zip": "62701",
        },
    },
    "Jane Smith": {
        "phone": "555-5678",
        "email": "janesmith@example.com",
        "address": {
            "street": "456 Oak Avenue",
            "city": "Shelbyville",
            "state": "IL",
            "zip": "62565",
        },
    },
}

john_email = address_book["John Doe"]["email"]
print(john_email)  # Output: 'johndoe@example.com'

# List of Dictionaries
students = [
    {"name": "John Doe", "age": 16, "grade": "11th", "favorite_subject": "Math"},
    {"name": "Jane Smith", "age": 17, "grade": "12th", "favorite_subject": "English"},
    {
        "name": "Emily Johnson",
        "age": 16,
        "grade": "11th",
        "favorite_subject": "Biology",
    },
]

jane_age = students[1]["age"]
print(jane_age)  # Output: 17


# ============= NESTED LOOPS =============

for i in range(1, 4):
    print("Outer loop incremented")
    for j in range(1, 4):
        print(f"i = {i}, j = {j}")
# Output:
# i = 1, j = 1
# i = 1, j = 2
# i = 1, j = 3
# i = 2, j = 1
# i = 2, j = 2
# i = 2, j = 3
# i = 3, j = 1
# i = 3, j = 2
# i = 3, j = 3

# Nested loops with matrix
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for row in matrix:
    for item in row:
        print(item, " ")
    print()  # Print a new line after each row
# Output:
# 1 2 3
# 4 5 6
# 7 8 9

# For loop with while loop
numbers = [3, 5, 2]

for num in numbers:
    print(f"Counting down from {num}:")
    while num >= 0:
        print(num)
        num -= 1
    print("---")
# Output:
# Counting down from 3:
# 3
# 2
# 1
# 0
# ---
# Counting down from 5:
# 5
# 4
# 3
# 2
# 1
# 0
# ---
# Counting down from 2:
# 2
# 1
# 0
# ---


# ============= SETS =============

# Creating Sets
my_set = {1, 2, 3, 4}
another_set = set([1, 2, 3, 4])
empty_set = set()  # Note: {} creates an empty dictionary, not a set

# Set Methods
my_set = {1, 2, 3}
my_set.add(4)  # {1, 2, 3, 4}
my_set.remove(2)  # {1, 3, 4}
# my_set.remove(5)  # Raises KeyError
my_set.discard(5)  # {1, 3, 4} - No error if element not found
my_set.clear()  # {}

# Set Operations
set1 = {1, 2, 3}
set2 = {3, 4, 5}

union_set = set1 | set2  # {1, 2, 3, 4, 5}
intersection_set = set1 & set2  # {3}
difference_set = set1 - set2  # {1, 2}
symmetric_difference_set = set1 ^ set2  # {1, 2, 4, 5}


# ============= SORTED FUNCTION =============

# Sorting in ascending order
lst = [1, 5, 3]
result = sorted(lst)
print(result)  # Output: [1, 3, 5]

# Sorting in descending order
lst = [1, 5, 3]
result = sorted(lst, reverse=True)
print(result)  # Output: [5, 3, 1]

# Sorting dictionary keys
my_dict = {"apple": 2, "banana": 3, "cherry": 1}
result = sorted(my_dict)
print(result)  # Output: ['apple', 'banana', 'cherry']

# Sorting strings by length
words = ["apple", "orange", "banana", "grape"]
result = sorted(words, key=len)
print(result)  # Output: ['apple', 'grape', 'orange', 'banana']


# Sorting by last character with custom function
def last_character(s):
    return s[-1]


words = ["apple", "banana", "cherry", "date"]
result = sorted(words, key=last_character)
print(result)  # Output: ['banana', 'apple', 'date', 'cherry']


# ============= LAMBDA FUNCTIONS =============

# Lambda with 1 argument
return_value = lambda x: x + 10
print(return_value(100))  # Prints 110

# Lambda with multiple arguments
return_value = lambda a, b: a + b
print(return_value(10, 20))  # Prints 30

# Lambda with sorted()
words = ["apple", "banana", "cherry", "date"]
result = sorted(words, key=lambda x: x[-1])
print(result)  # Output: ['banana', 'apple', 'date', 'cherry']


# ============= TERNARY OPERATORS =============

a = 10
b = 20

# Ternary operator
max_value = a if a > b else b

# Normal conditional (equivalent)
if a > b:
    max_value = a
else:
    max_value = b


# ============= DICTIONARY COMPREHENSIONS =============

# Map integers to their square
lst = [1, 2, 3, 4, 5, 6]
squares = {x: x**2 for x in lst}
print(squares)  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36}

# Converting list of tuples to dictionary
pairs = [("a", 1), ("b", 2), ("c", 3)]
dictionary = {key: value for key, value in pairs}
print(dictionary)  # {'a': 1, 'b': 2, 'c': 3}

# Even squares with condition
even_squares = {x: x**2 for x in range(1, 11) if x % 2 == 0}
print(even_squares)  # {2: 4, 4: 16, 6: 36, 8: 64, 10: 100}


# ============= TUPLES =============

# Creating tuples
my_tuple = ("Mario", "Luigi")
print(my_tuple)  # Prints ("Mario", "Luigi")

# Accessing tuple elements
my_tuple = ("Mario", "Luigi")
mario = my_tuple[0]
luigi = my_tuple[1]
print(mario)  # Prints "Mario"
print(luigi)  # Prints "Luigi"

# Tuples are immutable
my_tuple = (10, 20)
# my_tuple[0] = 30  # Results in TypeError: 'tuple' object does not support item assignment


# ============= BONUS SYNTAX (NOT ON ASSESSMENT) =============

# List Methods
lst.remove(x)  # Removes first element with value x

# Dictionary Methods
d.copy()  # Returns copy of dictionary

# Advanced Functions
from collections import defaultdict

# defaultdict() - Creates dictionary with default values for new keys

from collections import Counter

# Counter(x) - Creates frequency dictionary automatically

#! Difference between sorted and sort 