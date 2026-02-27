# problem 1


# def linear_search(items, target):
#     if target in items:
#         return print(items.index(target))
#     return print(-1)


# def linear_search2(items, target):
#     for i in range(len(items)):
#         if items(i) == target:
#             return i
#     return print(-1)


# items = ["haycorn", "haycorn", "haycorn", "hunny", "haycorn"]
# target = "hunny"
# linear_search(items, target)

# items = ["bed", "blue jacket", "red shirt", "hunny"]
# target = "red balloon"
# linear_search(items, target)


# problem 2
# """
# U- values are based off words
# P- make map for values
# I-
# """

# def final_value_after_operations(operations):
#     value_map = {
#         "bouncy":1,
#         "flouncy":1,
#         "trouncy":-1,
#         "pouncy":-1
#         }
#     start_val = 1
#     for word in operations:
#         if word in value_map:
#             start_val += value_map[word]
#     print(start_val)

# operations = ["trouncy", "flouncy", "flouncy"]
# final_value_after_operations(operations)

# operations = ["bouncy", "bouncy", "flouncy"]
# final_value_after_operations(operations)


# problem 3
# ? Answer key uses .replace but it is not on the cheatsheet
# ? should we use print or return
# ? example output does not match cheatsheet

# bottom version seems to be the more intended way
# def tiggerfy2(word):
#     new_word = word
#     substrings = ["t", "i", "gg", "er", "T", "I", "GG", "ER", "gG", "Gg", "eR"]
#     for sub in substrings:
#         new_word = new_word.replace(sub, "")

#     return new_word


# """
# iterate every idx in word
# if window is in substrings
#     move the iterator over
# append to new string in python
# """


# def tiggerfy(word):
#     new_word = word
#     substrings = ["t", "i", "gg", "er", "T", "I", "GG", "ER", "gG", "Gg", "eR"]
#     result = ""
#     i = 0
#     while i < len(word):
#         if i < len(word) - 1 and word[i : i + 2] in substrings:
#             i += 1
#         elif word[i] in substrings:
#             pass
#         else:
#             result += word[i]
#         i += 1

#     return result


# word = "Trigger"
# print(tiggerfy(word))

# word = "eggplant"
# print(tiggerfy(word))

# word = "Choir"
# print(tiggerfy(word))


#! Problem 4
#! DONE
#! Problem 2
class problem_:
    def function_name(self, param):
        pass

    def tests(self):
        pass


"""
check the number of violations
    if the number is more than 1, return false

    if theres a violation
        if the next number is less than the one before it
            return false

return true
"""


# def non_decreasing(nums):
#     count = 0
#     for idx in range(len(nums) - 1):
#         if nums[idx] > nums[idx + 1]:
#             count += 1
#             if count > 1:
#                 return False
#             if idx == 0 or nums[idx - 1] <= nums[idx + 1]:
#                 nums[idx] = nums[idx + 1]
#             else:
#                 nums[idx + 1] = nums[idx]

#     return True


# nums = [4, 2, 3]
# print(non_decreasing(nums))

# nums = [4, 2, 1]
# print(non_decreasing(nums))

# nums = [4, 4, 2, 3]
# print(non_decreasing(nums))

#! Problem 5: Missing Clues
"""
create tuple list 
iterate thru the range of values
create iterator for lower bound 
keep incrementing until we are 1 less than the clue
add the start and end to the tuple list
"""
# def find_missing_clues(clues, lower, upper):
#     result = []
#     clues.sort()
#     if lower < clues[0]:
#         result.append([lower, clues[0] - 1])

#     for i in range(len(clues) - 1):
#         if clues[i] + 1 != clues[i + 1]:
#             result.append([clues[i] + 1, clues[i + 1] - 1])

#     if clues[-1] < upper:
#         result.append([clues[-1] + 1, upper])

#     return print(result)


# clues = [0, 1, 3, 50, 75]
# lower = 0
# upper = 99
# find_missing_clues(clues, lower, upper)

# clues = [-1]
# lower = -1
# upper = -1
# find_missing_clues(clues, lower, upper)

# clues = [3, 50, 75]
# lower = 2
# upper = 99
# find_missing_clues(clues, lower, upper)


#! Problem 6: Vegetable Harvest
def harvest(vegetable_patch) -> int | None:
    count = 0
    for row in vegetable_patch:
        for j in range(len(row)):
            if row[j] == "c":
                count += 1
    return count


# vegetable_patch = [["x", "c", "x"], ["x", "x", "x"], ["x", "c", "c"], ["c", "c", "c"]]
# harvest(vegetable_patch)

# #! Problem 7: Eeyore's House

def good_pairs(pile1,pile2,k):
    pass

pile1 = [1,3,4]
pile2 = [1,3,4]
k = 1

pile1 = [1,2,4,12]
pile2 = [2,4]
k=3
good_pairs(pile1,pile2,k)

# #! Problem 8: Local Maximums

# def local_maximums(grid):
#     pass
