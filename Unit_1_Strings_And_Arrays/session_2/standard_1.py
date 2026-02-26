# Problem 1: Reverse Sentence (DONE)
"""
split the sentence by word
reverse the array
join into new sentence
"""


def reverse_sentence1(sentence):
    sent_arr = sentence.split(" ")
    sent_arr = sent_arr[::-1]
    new_arr = " ".join(sent_arr)
    print(new_arr)


def reverse_sentence(sentence):
    return " ".join(reversed(sentence.split(" ")))


# print(reverse_sentence("Hello How are u "))

# print("".join(reversed("Hello")))


#! Problem 2: Goldilocks Number (DONE)
"""
loop once to get the min and max values
loop again to return the first instance where neither are there
if this loop fails, return -1
"""


def goldilocks_approved1(nums):
    min_val = min(nums)
    max_val = max(nums)
    for num in nums:
        if len(nums) > 2 and (num != min_val or num != max_val):
            return num
    return -1


def goldilocks_approved(nums):
    if len(nums) <= 2:
        return -1
    min_val, max_val = nums[0], nums[0]
    for num in nums:
        if num < min_val:
            min_val = num
        if num > min_val:
            max_val = num

    for num in nums:
        if num != min_val or num != max_val:
            return num
    return -1


# nums = [3, 2, 1, 4]
# print(goldilocks_approved(nums))

# nums = [1, 2]
# print(goldilocks_approved(nums))

# nums = [2, 1, 3]
# print(goldilocks_approved(nums))

#! Poblem 3: Delete Minimum
"""
loop thru array until its len 0 
use remove function for min 

"""


def delete_minimum_elements(hunny_jar_sizes):
    newlst = []
    while len(hunny_jar_sizes) > 0:
        newlst.append(min(hunny_jar_sizes))
        hunny_jar_sizes.remove(min(hunny_jar_sizes))
    return print(newlst)


# hunny_jar_sizes = [5, 3, 2, 4, 1]
# print(delete_minimum_elements(hunny_jar_sizes))

# hunny_jar_sizes = [5, 2, 1, 8, 2]
# delete_minimum_elements(hunny_jar_sizes)

#! Problem 4: Sum of Digits
"""
"""
import math


def sum_of_digits(num):
    result = 0
    while num > 0:
        result += num % 10
        num = math.floor(num / 10)
    print(result)


# num = 423
# sum_of_digits(num)

# num = 4
# sum_of_digits(num)


#! Problem 5: Bouncy Flouncy
def final_value_after_operations(operations):
    value_map = {
        "bouncy": 1,
        "flouncy": 1,
        "trouncy": -1,
        "pouncy": -1,
    }
    result = 1
    for operation in operations:
        if operation in value_map:
            result += value_map[operation]
    return print(result)


# operations = ["trouncy", "flouncy", "flouncy"]
# final_value_after_operations(operations)

# operations = ["bouncy", "bouncy", "flouncy"]
# final_value_after_operations(operations)


#! Problem 6: Acronym
"""
loop through every word
grab first char and concetnate 
early check if length exceeds input 
if it matches input return false or true


return err if empty list 
if list ele not a string
if list input is empty 
"""


def is_acronym(words: list[str], s: str) -> bool:
    if type(s) != str or not isinstance(words, list):
        print("Invalid")
        return False
    # if isinstance(s,str) == False:
    #     return False

    if len(s) < 1 or len(words) < 1:
        return False
    if len(s) != len(words):
        return False

    result = []
    for word in words:
        result.append(word[0])

    newresult = "".join(result)
    return print(newresult == s)


# words = ["christopher", "rob", "milne"]
# s = "crm"
# print(is_acronym(words, s))


#! Problem 7: Good Things Come in Threes
# ? This question definitely feels incompletplety worded and i do not like it, solution too feels kinda too complex at the same time
def make_divisible_by_3(nums):
    result = 0
    for num in nums:
        if num % 3 != 0:
            result += 1
    return print(result)


# nums = [1, 2, 3, 4]
# make_divisible_by_3(nums)

# nums = [3, 6, 9]
# make_divisible_by_3(nums)

#! Problem 8: Exclusive Elements
"""
iterate thru each list one at a time 
add to the list if its not in the other one 
return the list 

use exclusive or on sets 
"""


def exclusive_elemts1(lst1, lst2):
    result = []
    for ele in lst1:
        if ele not in lst2:
            result.append(ele)
    for ele in lst2:
        if ele not in lst1:
            result.append(ele)
    return print(result)


def exclusive_elemts(lst1, lst2):
    print(list(set(lst1) ^ set(lst2)))


# lst1 = ["pooh", "roo", "piglet"]
# lst2 = ["piglet", "eeyore", "owl"]
# exclusive_elemts(lst1, lst2)

# lst1 = ["pooh", "roo"]
# lst2 = ["piglet", "eeyore", "owl", "kanga"]
# exclusive_elemts(lst1, lst2)

# lst1 = ["pooh", "roo", "piglet"]
# lst2 = ["pooh", "roo", "piglet"]
# exclusive_elemts(lst1, lst2)


#! Problem 9: Merge Strings Alternately
"""
use ptr2 technique from the same side 
use and while loop 

"""
def merge_alternately(word1, word2):

    wrd1ptr = 0
    wrd2ptr = 0
    result = []

    while wrd1ptr < len(word1) - 1 and wrd2ptr < len(word2) - 1:
        result.append(word1[wrd1ptr])
        result.append(word1[wrd2ptr])
        wrd1ptr += 1
        wrd2ptr += 1



#! Problem 10: Eeyore's House
def good_pairs(pile1, pile2, k):
    pass
