# Python Quick Reference Guide - CodePath TIP102 Unit 3

# ============= STACKS =============

# Stack - Last In, First Out (LIFO)
# Like a stack of plates - add/remove from top

stack = []

# Push items onto stack (add to top)
stack.append(1)
stack.append(2)

# Pop item from stack (remove from top)
popped_item = stack.pop()
print(popped_item)  # Prints: 2
print(stack)  # Prints: [1]

# When to use stacks:
# - Reversing data
# - Balancing symbols (parentheses, brackets)
# - Backtracking
# - Expression evaluation


# ============= QUEUES =============

# Queue - First In, First Out (FIFO)
# Like a line of people - first person in line exits first

from collections import deque

# Initialize queue
queue = deque()

# Add element to end (right side) of queue
queue.append(1)
queue.append(2)

# Remove element from beginning (left side) of queue
removed_elt = queue.popleft()
print(removed_elt)  # Prints 1

# Alternative: Add to left, remove from right
queue = deque()
queue.appendleft(1)
queue.appendleft(2)
removed_elt = queue.pop()
print(removed_elt)  # Prints 1

# When to use queues:
# - Processing items in order
# - Breadth First Search (BFS)
# - Round-robin scheduling


# ============= TWO POINTER TECHNIQUE =============

# Opposite Direction Pointers (e.g., reverse, palindrome)
left_pointer = 0
right_pointer = len(word) - 1
while left_pointer < right_pointer:
    # Swap or compare elements
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

# When to use two-pointer:
# - Working with strings, arrays, linked lists
# - Reducing nested loops
# - Searching for pairs/triplets
# - In-place operations
# - Comparing opposite ends of sequence
# - Partitioning problems


# ============= HELPER FUNCTIONS =============

# Helper functions perform subtasks of main function
# Follows Single Responsibility Principle (SRP)


# Helper Function: Calculate price of one item
def calculate_price(item_price, quantity):
    return item_price * quantity


# Primary Function: Calculate total cost of bill
def calculate_total(bill):
    total = 0
    for item_price, quantity in bill.items():
        total += calculate_price(item_price, quantity)  # Call helper
    return total


# ============= UNPACKING =============

# Assign multiple variables at once
a, b = 1, 2

# Swap values (common in two-pointer)
pointer_one, pointer_two = pointer_two, pointer_one

# Swap values in list
nums[pointer_one], nums[pointer_two] = nums[pointer_two], nums[pointer_one]

# Unpack from list
inventory = [["apples", 3], ["carrots", 5]]
[[item, quantity], [item2, quantity2]] = inventory
# item = "apples", quantity = 3
# item2 = "carrots", quantity2 = 5


# ============= INNER FUNCTIONS =============

# Inner/Nested Functions - Function defined inside another function
# Inner function has access to outer function's variables/parameters
# Only available within scope of outer function


# Outer function
def print_sum(x, y):
    # Inner function
    def get_sum():
        return x + y  # Has access to x and y

    total = get_sum()
    print(f"{x} + {y} is {total}")


print_sum(1, 2)  # Prints: 1 + 2 is 3


# Example with helper logic
def total_sum_of_digits(numbers):
    # Inner function to calculate sum of digits of single number
    def sum_of_digits(n):
        total = 0
        while n > 0:
            total += n % 10
            n //= 10
        return total

    # Main function logic
    total_sum = 0
    for number in numbers:
        total_sum += sum_of_digits(number)

    return total_sum


# ============= BONUS: STACKS VS QUEUES =============

# Stack problems often use recursion (uses call stack)
# Queue problems generally use iteration (while loops)


# Reverse string - Iterative stack solution
def reverse_string_iterative(s):
    stack = []

    # Push all characters onto stack
    for char in s:
        stack.append(char)

    reversed_string = ""

    # Pop all characters from stack
    while stack:
        reversed_string += stack.pop()

    return reversed_string


# Reverse string - Recursive stack solution
def reverse_string_recursive(s):
    # Base case
    if len(s) <= 1:
        return s

    # Recursive case: reverse rest + append first char to end
    return reverse_string_recursive(s[1:]) + s[0]
