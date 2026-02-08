
python
# Python Quick Reference Guide - CodePath TIP102 Unit 4

# ============= BIG O NOTATION (ASYMPTOTIC ANALYSIS) =============

# Big O measures how algorithm performance changes as input size grows
# Two components: Time Complexity and Space Complexity
# Usually evaluate WORST CASE performance

# Common Time Complexities (from fastest to slowest):
# O(1)       - Constant
# O(log n)   - Logarithmic
# O(n)       - Linear
# O(n log n) - Log Linear
# O(n²)      - Quadratic
# O(2ⁿ)      - Exponential


# ============= TIME COMPLEXITY =============

# Constant Time - O(1)
# Same number of operations regardless of input size
def add_from_1_to_n(n):
    return (n * (n + 1)) / 2
# Whether n=1 or n=1,000,000, same operations performed


# Linear Time - O(n)
# Operations proportional to input size
def add_from_1_to_n(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total
# If n doubles, runtime roughly doubles


# Sequential Operations - Add complexities, drop constants
def count_up_and_down(n):
    # Takes O(n) time
    for i in range(1, n + 1):
        print(i)
    
    # Takes O(n) time
    for i in range(n, 0, -1):
        print(i)
# O(n) + O(n) = O(2n) => O(n)
# Drop coefficients: O(n + 1) => O(n)


# Quadratic Time - O(n²)
# Nested loops - multiply iterations
def duplicates_within_k(numbers, k):
    lst_length = len(numbers)
    
    if lst_length < 2 or k == 0:
        return False
    
    for i in range(lst_length):  # O(n)
        j = i + 1
        dist_remaining = k
        while dist_remaining > 0 and j < lst_length:  # O(n) worst case
            if numbers[i] == numbers[j]:
                return True
            j += 1
            dist_remaining -= 1
    return False
# Outer loop: n iterations
# Inner loop: n-1 iterations (worst case)
# Total: n * (n-1) = n² - n => O(n²)


# ============= SPACE COMPLEXITY =============

# Rules for Space Complexity:
# - Single-value variables (int, float, bool): O(1)
# - Strings: O(n) where n = string length
# - Lists: O(n) where n = list length
# - Dictionaries: O(n) where n = number of key-value pairs
# - Don't count input space (passed as arguments)
# - Only count variables created INSIDE the function


# Constant Space - O(1)
# Fixed number of variables regardless of input size
def sum_array(arr):
    total = 0  # O(1) space
    for num in arr:  # num is O(1) space
        total += num
    return total
# Only creates 'total' and 'num' variables (both O(1))
# Input 'arr' doesn't count (created outside function)


# Linear Space - O(n)
# New data structure proportional to input size
def copy_array(arr):
    copy = []  # O(n) space where n = len(arr)
    for num in arr:
        copy.append(num)
    return copy
# Creates new list 'copy' of size n


# Quadratic Space - O(n²)
# Nested data structures
def init_matrix(n):
    matrix = []
    for row in range(n):
        matrix.append([])
        for col in range(n):
            matrix[row].append(None)
    return matrix
# Creates n lists of length n = O(n²)

def all_pairs(arr):
    n = len(arr)
    pairs = []
    for i in range(n):
        for j in range(n):
            pairs.append((arr[i], arr[j]))
    return pairs
# Creates n² pairs = O(n²) space


# ============= BUILT-IN FUNCTION COMPLEXITIES =============

# Common built-in time complexities (not required to memorize):
len(sequence)          # O(1)
sequence[idx]          # O(1)
sequence[idx:idx+k]    # O(k)
sequence.sort()        # O(n log n)
sorted(sequence)       # O(n log n)
sequence.copy()        # O(n)
lst.append(item)       # O(1)
lst.pop()              # O(1)
lst.insert(idx, item)  # O(n)
dict.get(key)          # O(1)
dict.pop(key)          # O(1)


# Example: Accounting for built-in function complexity
def kth_smallest_element(arr, k):
    arr.sort()  # O(n log n)
    return arr[k-1]  # O(1)
# Overall time complexity: O(n log n)


# ============= ADVANCED: MULTIPLE VARIABLES =============

# Use separate variables when multiple inputs affect complexity
def init_matrix(rows, columns):
    matrix = []
    for r in range(rows):  # O(m) where m = rows
        matrix.append([])
        for c in range(columns):  # O(n) where n = columns
            matrix[r].append(None)
    return matrix
# Time Complexity: O(m * n) where m=rows, n=columns
# Space Complexity: O(m * n)

# Don't assume m = n! Could have 1 row and 1000 columns.
# Always clearly define what your Big O variables represent.


# ============= BIG O SIMPLIFICATION RULES =============

# 1. Drop constants
# O(2n) => O(n)
# O(n + 100) => O(n)

# 2. Drop non-dominant terms
# O(n² + n) => O(n²)
# O(n + log n) => O(n)

# 3. Different inputs use different variables
# O(m + n) NOT O(2n) when m and n are separate inputs

# 4. Nested loops multiply
# Two nested loops over n: O(n²)
# Loop over m, nested loop over n: O(m * n)
```