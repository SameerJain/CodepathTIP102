# Python Quick Reference Guide - CodePath TIP102

# ============= BUILT-IN FUNCTIONS =============

# Print - Prints message to console
print("Welcome to TIP102!")  # Prints "Welcome to TIP102!"
print(100)  # Prints 100
s = "Welcome to CodePath!"
print(s)  # Prints "Welcome to CodePath!"
lst = ["TIP101", "TIP102", "TIP103"]
print(lst)  # Prints ["TIP101", "TIP102", "TIP103"]
x, y = 5, 3
print(x + y)  # Prints 8

# Length - Returns length of list or string
lst = ["a", "b", "c"]
print(len(lst))  # Output: 3
s = "abcd"
print(len(s))  # Output: 4

# Range - Returns sequence of numbers
range(10)  # 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
range(1, 11)  # 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
range(0, 30, 5)  # 0, 5, 10, 15, 20, 25

# Sum - Returns sum of all values in list
sum([1, 2, 3, 4])  # Evaluates to 10

# Min - Returns minimum value
min([2, 3, 4, 1, 5])  # Evaluates to 1
min(5, 2, 3)  # Evaluates to 2
min(["a", "b", "c", "aa"])  # Evaluates to 'a'

# Max - Returns maximum value
max([2, 3, 5, 1, 4])  # Evaluates to 5
max(5, 2, 3)  # Evaluates to 5
max(["a", "b", "c", "aa"])  # Evaluates to 'c'

# Enumerate - Adds counter to iterable
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

# Zip - Combines multiple iterables into tuples
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
zipped = zip(names, ages)
print(list(zipped))  # Prints [('Alice', 25), ('Bob', 30), ('Charlie', 35)]

names = ["Alice", "Bob", "Charlie", "David"]
ages = [25, 30, 35]
zipped = zip(names, ages)
print(list(zipped))  # Prints [('Alice', 25), ('Bob', 30), ('Charlie', 35)]


# ============= LIST METHODS =============

# Append - Adds item to end of list
lst = [1, 2, 3, 4]
lst.append(5)
print(lst)  # Prints [1, 2, 3, 4, 5]

# Sort - Sorts list in ascending order
lst = [4, 2, 1, 3]
lst.sort()
print(lst)  # Prints [1, 2, 3, 4]

lst = ["b", "a", "d", "c"]
lst.sort()
print(lst)  # Prints ['a', 'b', 'c', 'd']


# ============= STRING METHODS =============

# Lower - Returns lowercase string
s = "Hello World!"
lowered = s.lower()
print(lowered)  # Prints 'hello world!'

s = "HELLO WORLD"
lowered = s.lower()
print(lowered)  # Prints 'hello world'

# Split - Splits string into list
s = "Never gonna give you up"
split = s.split()
print(split)  # Prints ['Never', 'gonna', 'give', 'you', 'up']

s = "Never-gonna-let-you-down"
split = s.split("-")
print(split)  # Prints ['Never', 'gonna', 'let', 'you', 'down']

# Join - Turns iterable into string with separator
lst = ["Never", "gonna", "run", "around", "and", "desert", "you"]
joined = " ".join(lst)
print(joined)  # Prints 'Never gonna run around and desert you'

lst = ["Never", "gonna", "make", "you", "cry"]
joined = "-".join(lst)
print(joined)  # Prints 'Never-gonna-make-you-cry'

# Strip - Removes whitespace or characters from ends
s = "       Never gonna say goodbye       "
stripped = s.strip()
print(stripped)  # Prints 'Never gonna say goodbye'

s = "????Never gonna tell a lie and hurt you?????"
stripped = s.strip("?")
print(stripped)  # Prints 'Never gonna tell a lie and hurt you'


# ============= BASIC SYNTAX =============

# Variables (no declaration needed, dynamically typed)
var1 = 10
var2 = "Codepath"
my_boolean = True
print(var1)  # Prints 10
print(var2)  # Prints 'Codepath'
print(my_boolean)  # Prints True

x = 10
print(x)  # Prints 10
x = "Hello"
print(x)  # Prints 'Hello'

# Conditionals
x = 3
if x > 1:
    print("This line will execute!")
if x > 5:
    print("This line will not execute!")
# Output: 'This line will execute!'

x = 10
y = 20
if x > y:
    print("x is greater than y")
elif y > x:
    print("y is greater than x")
# Output: 'y is greater than x'

x = 20
y = 20
if x > y:
    print("x is greater than y")
elif y > x:
    print("y is greater than x")
else:
    print("x and y are equal")
# Output: 'x and y are equal'


# Functions
def function_example():
    print("Hello world!")


function_example()  # Prints 'Hello world!'


def function_w_parameters(parameter1, parameter2):
    print("Parameter 1: ", parameter1)
    print("Parameter 2: ", parameter2)


function_w_parameters("Interview", "Prep")
# Output:
# Parameter 1: Interview
# Parameter 2: Prep


def sum(a, b):
    return a + b


def sum_without_returning(a, b):
    a + b


return_val1 = sum(4, 2)
return_val2 = sum_without_returning(4, 2)
print(return_val1)  # Output: 6
print(return_val2)  # Output: None

# F-strings - Insert variables into strings
name = "Michael"
print(f"Welcome to Codepath, {name}!")  # Prints 'Welcome to CodePath, Michael!'

a = 3
b = 5
print(f"The sum of {a} and {b} is {a + b}")  # Prints 'The sum of 3 and 5 is 8'

# Modulo (remainder division)
print(5 % 2)  # Prints 1 because 5 / 2 = 2 remainder 1
print(10 % 2)  # Prints 0 because 10 / 2 = 5 remainder 0


# ============= LOOPS =============

# For Loops - Iterate over sequence
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)  # Outputs each fruit on a new line

for i in range(5):
    print(i)  # Prints numbers 0 to 4

# While Loops - Iterate while condition is True
user_input = ""
while user_input != "quit":
    user_input = input("Enter a command (type 'quit' to exit): ")
print("You exited the loop.")

i = 1
while i < 6:
    print(i)
    i += 1


# ============= NESTED STRUCTURES =============

# Nested Lists
singers = ["Sabrina Carpenter", "FKA Twigs", "Elliot Smith"]

albums = [
    ["Sabrina Carpenter", "Short n' Sweet"],
    ["FKA Twigs", "Magdalene"],
    ["Elliot Smith", "Either/Or"],
]

numbers = [[1], [1, 2], [1, 2, 3]]

water_levels = ["Shallow", ["Deep", ["Deeper"]]]

# Matrix (nested list with equal-length inner lists)
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

# Nested Loops
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

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for row in matrix:
    for item in row:
        print(item, " ")
    print()  # Print a new line after each row
# Output:
# 1 2 3
# 4 5 6
# 7 8 9

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


# ============= LIST COMPREHENSIONS =============

# Basic list comprehension
nums = [1, 2, 3, 4, 5]
doubled = [value * 2 for value in nums]
print(doubled)  # Output: [2, 4, 6, 8, 10]

# List comprehension with condition
words = ["I", "Love", "Codepath!"]
result = [word for word in words if len(word) > 5]
print(result)  # Output: ['Codepath!']


# ============= TWO POINTER TECHNIQUE =============

# Opposite Direction Pointers (e.g., reverse, palindrome)
left_pointer = 0
right_pointer = len(word) - 1
while left_pointer < right_pointer:
    pass  # Swap or compare elements
    left_pointer += 1
    right_pointer -= 1

# Same Direction Pointers (e.g., merge sorted lists)
nums1_pointer = 0
nums2_pointer = 0
while nums1_pointer < len(nums1) and nums2_pointer < len(nums2):
    if condition:
        # operation
        nums1_pointer += 1
    else:
        # operation
        nums2_pointer += 1


# ============= STRING VS LIST DIFFERENCES =============

# Strings are IMMUTABLE (cannot be changed)
s = "Try"
# s[0] = 'C'  # Results in TypeError: 'str' object does not support item assignment

# Lists are MUTABLE (can be changed)
lst = ["T", "r", "y"]
lst[0] = "C"
print(lst)  # Prints ['C', 'r', 'y']


# ============= BONUS SYNTAX (NOT ON ASSESSMENT) =============

# List Methods
lst.insert(0, item)  # Insert item at index 0
lst.remove(item)  # Remove first occurrence of item
lst.pop(2)  # Remove and return element at index 2
new_lst = lst.copy()  # Create copy of list

# Math
abs(-5)  # Returns 5

# String Methods
s.isalpha()  # Returns True if all chars are letters (a-z)
s.isalnum()  # Returns True if all chars are alphanumeric (a-z or 0-9)
s.find("x")  # Returns start index of first occurrence of "x" (or -1 if not found)
s.count("x")  # Returns frequency of substring "x"

# Sets - Unordered, no duplicates
my_set = {1, 2, 3, 3, 4}  # {1, 2, 3, 4}
