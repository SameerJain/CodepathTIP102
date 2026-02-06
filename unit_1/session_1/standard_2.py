# # problem 1
# def batman():
#     print("I am vengeance. I am the night. I am Batman!")

# batman()

# problem 2
# def madlib(verb):
#     print(f"I have one powerm I never {verb}.- Batman")

# verb = "give up"
# madlib(verb)

# verb = "nap"
# madlib(verb)

# problem 3

# def trilogy(year):
#     movie_map = {2005:"Batman Begins",2008:"The Dark Knight",2012:"The Dark Knight Rises"}
#     no_movie = "Christopher Nolan did not release a Batman movie in 1998."

#     return movie_map[year] if year in movie_map else no_movie

# year = 2008
# print(trilogy(year))

# year = 1998
# print(trilogy(year))

# problem 4
# def get_last(items):
#     if not items:
#         return print(None)
#     return print(items[-1])


# items = ["spider man", "batman", "superman", "iron man", "wonder woman", "black adam"]
# get_last(items)

# items = []
# get_last(items)


# problem 5
# def concatenate(words):
#     starter_word = ""
#     for word in words:
#         starter_word += word
#     return print(starter_word)


# words = ["vengeance", "darkness", "batman"]
# concatenate(words)

# words = []
# concatenate(words)


# problem 6
# def squared(numbers):
#     for i in range(len(numbers)):
#         numbers[i] **= 2
#     return numbers
# #? can this be done with list comprehension

# numbers = [1, 2, 3]
# print(squared(numbers))

# problem 7
# def nanana_batman(x):
#     starter_word = "batman"
#     while x != 0:
#         starter_word = "na" + starter_word
#         x -= 1
#     print(starter_word)

# x = 6
# nanana_batman(x)

# x = 0
# nanana_batman(x)


# problem 8
# def find_villain(crowd, villain):
#     idx_list = []
#     for i in range(len(crowd)):
#         if crowd[i] == villain:
#             idx_list.append(i)
#     return print(idx_list)


# crowd = [
#     "Batman",
#     "The Joker",
#     "Alfred Pennyworth",
#     "Robin",
#     "The Joker",
#     "Catwoman",
#     "The Joker",
# ]
# villain = "The Joker"
# find_villain(crowd, villain)

# problem 9
# def get_odds(nums):
#     ans_list = []
#     for num in nums:
#         if num % 2 == 1:
#             ans_list.append(num)
#     return print(ans_list)


# nums = [1, 2, 3, 4]
# get_odds(nums)

# nums = [2, 4, 6, 8]
# get_odds(nums)


# problem 10
# def up_and_down(lst):
#     even_count = 0
#     odd_count = 0
#     for ele in lst:
#         if ele % 2 == 0:
#             even_count += 1
#         else:
#             odd_count += 1
#     return print(odd_count - even_count)


# lst = [1, 2, 3]
# up_and_down(lst)

# lst = [1, 3, 5]
# up_and_down(lst)

# lst = [2, 4, 10, 2]
# up_and_down(lst)

# problem 11
"""
track sum for
"""
# def running_sum(superhero_stats):
#     sum_count = 0
#     for idx, month in enumerate(superhero_stats):
#         print("\n\niter")
#         print(f"idx:{idx},month:{month}, sum_count:{sum_count}")
#         sum_count += month
#         print(f"idx:{idx},month:{month}, sum_count:{sum_count}")
#         month = sum_count
#         superhero_stats[idx] = month
#         print(f"idx:{idx},month:{month},sum_count: {sum_count}")
#         print("Current: ",superhero_stats)
#     return print("Final:\n", superhero_stats)


# superhero_stats = [1, 2, 3, 4]
# running_sum(superhero_stats)

# superhero_stats = [1, 1, 1, 1, 1]
# running_sum(superhero_stats)

# superhero_stats = [3, 1, 2, 10, 1]
# running_sum(superhero_stats)

# Problem 12
"""
Get median idx
add each element to new list 
iterate for half of list size 
turn old list into new list 
"""


def shuffle(cards):
    start_idx = 0
    mid_idx = len(cards) // 2
    new_lst = []

    while mid_idx != len(cards):
        if start_idx != len(cards) // 2:
            new_lst.append(cards[start_idx])
            start_idx += 1
        new_lst.append(cards[mid_idx])
        mid_idx += 1

    cards = new_lst

    return print(cards)


def shuffle2(cards):
    n = len(cards) // 2
    shuffled = []

    for i in range(n):
        shuffled.append(cards[i])
        shuffled.append(cards[i + n])
    if i < len(cards) // 2:
        shuffled.append(cards[-1])
    return print(shuffled)


# cards = ["Joker", "Queen", 2, 3, "Ace", 7]
# shuffle(cards)

# cards = [9, 2, 3, "Joker", "Joker", 3, 2, 9]
# shuffle(cards)

cards = [10, 10, 2, 2, 3]
shuffle2(cards)

