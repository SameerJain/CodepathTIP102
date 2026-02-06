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


# def non_decreasing(nums):
#     errors = 0
#     for i in range(len(nums) - 1):
#         if nums[i] > nums[i + 1]:
#             errors += 1
#             if errors > 1:
#                 return False
#             if i == 0 or nums[i - 1] > nums[i + 1]:
#                 nums[i + 1] = nums[i]
#             else:
#                 nums[i] = nums[i + 1]

#     return True


# nums = [4, 2, 3]
# print(non_decreasing(nums))

# nums = [4, 2, 1]
# print(non_decreasing(nums))

# nums = [3, 4, 2, 3]

# problem 5

"""
create tuple list 
iterate thru the range of values
create iterator for lower bound 
keep incrementing until we are 1 less than the clue
add the start and end to the tuple list
"""
def find_missing_clues(clues,lower,upper):
    tuple_list = []
    i = lower
    while i <= upper:
        start = i
        i+=1
        if i in clues:
            tuple_list.append([start,i-1])

    return tuple_list

clues = [0, 1, 3, 50, 75]
lower = 0
upper = 99
print(find_missing_clues(clues, lower, upper))

clues = [-1]
lower = -1
upper = -1
(find_missing_clues(clues, lower, upper))
