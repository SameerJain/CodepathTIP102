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
# # ? can this be done with list comprehension

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

def get_odds(nums):
    pass 

nums = [1, 2, 3, 4]
get_odds(nums)

nums = [2, 4, 6, 8]
get_odds(nums)
