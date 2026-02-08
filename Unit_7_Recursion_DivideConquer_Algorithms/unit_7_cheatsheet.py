# Python Quick Reference Guide - CodePath TIP102 Unit 7

# ============= RECURSION BASICS =============

# Recursion - Function calling itself


# Infinite recursion (will crash!)
def recursive_crash():
    print("I will run forever")
    recursive_crash()


# Iteration vs Recursion:
# - Iteration: Bottom-up (start small, build up)
# - Recursion: Top-down (break down, then build up)


# Iterative Example
def count_iterative(num):
    i = 1
    while i <= num:
        print(f"Count {i}!")
        i += 1


# Input: 5
# Output: Count 1!, Count 2!, Count 3!, Count 4!, Count 5!


# Recursive Example
def count_recursive(num):
    print(f"Count {num}!")
    if num == 1:
        return
    else:
        count_recursive(num - 1)


# Input: 5
# Output: Count 5!, Count 4!, Count 3!, Count 2!, Count 1!


# ============= BUILDING RECURSIVE FUNCTIONS =============

# Every recursive function needs:
# 1. Base Case - When to stop recursing
# 2. Recursive Case - Call function again with smaller/simpler input


def count_recursive(num):
    # Action to repeat
    print(f"Count {num}!")

    # Base Case: Stop when num is 1
    if num == 1:
        return

    # Recursive Case: Continue with smaller input
    else:
        count_recursive(num - 1)


# Multiple Base Cases
def is_odd(n):
    # Base Case 1: n is 0 (not odd)
    if n == 0:
        return False

    # Base Case 2: n is 1 (is odd)
    if n == 1:
        return True

    # Recursive Case
    else:
        return is_odd(n - 2)


print(is_odd(5))  # Prints True
print(is_odd(6))  # Prints False


# Multiple Recursive Cases
def count_evens(lst):
    # Base Case: Empty list
    if not lst:
        return 0

    # Recursive Case 1: First element is even
    if lst[0] % 2 == 0:
        return 1 + count_evens(lst[1:])

    # Recursive Case 2: First element is odd
    else:
        return count_evens(lst[1:])


print(count_evens([1, 2, 3, 4]))  # Prints 2


# Return statement acts as "accumulator variable" in recursion
# Combines current value with results of recursive calls


# ============= RECURSIVE DRIVER & HELPER FUNCTIONS =============

# Use helper function to pass extra data to recursive calls


# Driver Function - Makes first call with initial values
def partition_evens_odds(lst):
    return recurse_partition(lst, [], [])


# Helper Function - Does the recursive work
def recurse_partition(lst, evens, odds):
    if not lst:
        return evens, odds
    if lst[0] % 2 == 0:
        evens.append(lst[0])
    else:
        odds.append(lst[0])
    return recurse_partition(lst[1:], evens, odds)


lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
evens, odds = partition_evens_odds(lst)
print(evens)  # Prints: [2, 4, 6, 8]
print(odds)  # Prints: [1, 3, 5, 7, 9]

# Why use helper? Provides better user experience
# User doesn't need to pass empty lists as arguments


# ============= DIVIDE & CONQUER ALGORITHMS =============

# Three steps:
# 1. DIVIDE - Break problem into smaller subproblems
# 2. CONQUER - Solve each subproblem (often using recursion)
# 3. COMBINE - Merge solutions to find final answer


# ============= BINARY SEARCH =============

# Classic divide & conquer algorithm
# Finds target in sorted list by dividing in half each step
# Time Complexity: O(log n)


def binary_search(numbers, value):
    low = 0
    high = len(numbers) - 1

    while low <= high:
        mid = (low + high) // 2

        if numbers[mid] > value:
            high = mid - 1  # Search left half
        elif numbers[mid] < value:
            low = mid + 1  # Search right half
        else:
            return mid  # Found it!

    return None  # Not found


# Steps:
# 1. Check middle value
# 2. If middle == target, return index
# 3. If target < middle, search left half
# 4. If target > middle, search right half
# 5. Repeat until found or list exhausted


# ============= MERGE SORT =============

# Classic divide & conquer sorting algorithm
# Time Complexity: O(n log n)


def merge_sort(arr):
    # Base case: array of 0 or 1 elements already sorted
    if len(arr) <= 1:
        return arr

    # Divide: Split array in half
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    # Combine: Merge sorted halves
    return merge(left_half, right_half)


def merge(left, right):
    result = []
    i = 0  # Pointer for left
    j = 0  # Pointer for right

    # Compare and merge in sorted order
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Append remaining elements
    result.extend(left[i:])
    result.extend(right[j:])

    return result


# Steps:
# 1. Divide list into halves until sublists of length 1
# 2. Conquer by sorting each sublist (length 1 already sorted)
# 3. Combine by merging sorted sublists together


# ============= LOGARITHMIC TIME COMPLEXITY - O(log n) =============

# What is a log?
# Inverse of exponent
# log₂(8) = 3 because 2³ = 8
# log₁₀(10000) = 4 because 10⁴ = 10000

# When do we see O(log n)?
# When input size is divided by constant rate each iteration

# Binary Search Example:
# Input size 8  → 3 iterations max
# Input size 16 → 4 iterations max
# Input size 32 → 5 iterations max
# Doubling input only adds 1 more iteration!

# General rule:
# If dividing input by X each iteration → log base X
# Most common is log base 2 (dividing by 2)
# Big O notation doesn't specify base: just O(log n)


# ============= LOG-LINEAR TIME COMPLEXITY - O(n log n) =============

# Represents:
# - n: Linear pass through all elements
# - log n: Number of times input is split/reduced

# Common in: Merge Sort, Quick Sort

# Merge Sort breakdown:
# - Dividing array: O(log n) - split until length 1
# - Merging subarrays: O(n) - compare all elements
# - Total: O(n) × O(log n) = O(n log n)


# ============= EXPONENTIAL TIME COMPLEXITY - O(2ⁿ) =============

# Runtime doubles with each addition to input
# Very inefficient - avoid when possible
# Common in: Naive recursion, exhaustive searches


# Naive Fibonacci Example
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)


# Each call makes 2 more calls → exponential growth
# fib(5) makes 1 call → 2 calls → 4 calls → 8 calls...


# ============= THE CALL STACK =============

# Call Stack - Tracks order of function calls using stack
# - New function call → added to top of stack
# - Function finishes → removed from stack
# - Computer always executes top function first


# Example: Nested function calls
def function_c():
    print("I'm Function C!")
    print("Function C is done executing!")


def function_b():
    print("I'm Function B!")
    function_c()
    print("Function B is done executing!")


def function_a():
    print("I'm Function A!")
    function_b()
    print("Function A is done executing!")


function_a()
# Output:
# I'm Function A!
# I'm Function B!
# I'm Function C!
# Function C is done executing!
# Function B is done executing!
# Function A is done executing!


# ============= RECURSION & SPACE COMPLEXITY =============

# Call stack takes up memory!
# Each function call = element in stack

# Space complexity affected by number of recursive calls


# Example: Sum 0 to n
def sum_zero_to_n(n):
    if n == 0:
        return 0
    return n + sum_zero_to_n(n - 1)


# Makes n recursive calls before returning
# Space Complexity: O(n)

# Non-recursive functions usually use O(1) space for call stack
