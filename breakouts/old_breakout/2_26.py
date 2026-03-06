"""
U- Reverse the string
P- .split to turn the sentence into array
    reverse the order of the array
    join the array back into 1 string
I-
"""


# def reverse_sentence(sentence):
#     new_sentence = sentence.split(" ")
#     # new_sentence = new_sentence[::-1]
#     newlst = []
#     for i in range(len(new_sentence) - 1, -1, -1):
#         newlst.append(new_sentence[i])
#     newlst = " ".join(newlst)
#     return newlst


# sentence = "tubby little cubby all stuffed with fluff"
# print(reverse_sentence(sentence))

# sentence = "Pooh"
# print(reverse_sentence(sentence))

lst = [1,2,3,4,5]
print(lst.pop(-1))
print(lst)
