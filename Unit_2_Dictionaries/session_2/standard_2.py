
#! Problem 1: Most endangered species 

"""
sort by lowest value for population 
"""




def most_endangered0(species_list):
    species_list.sort(key=lambda species_list: species_list["population"])
    return species_list

def most_endangered(species_list):
    newdict = []
    for species in species_list:
        minpop = float("inf")
        for curr in species_list:
            if curr["population"] <= minpop:
                minspec = curr
        newdict.append(minspec)
        species_list.remove(minspec)
    return newdict

species_list = [
    {"name": "Amur Leopard",
     "habitat": "Temperate forests",
     "population": 84
    },
    {"name": "Javan Rhino",
     "habitat": "Tropical forests",
     "population": 72
    },
    {"name": "Vaquita",
     "habitat": "Marine",
     "population": 10
    }
]

print(most_endangered(species_list))

#! Problem 2: Identifying endangered species 

"""
method 1
use n^2 approach 
iterate through second list for each character 
if there is a match then do count ++

method 2
convert the first list into a set for a o(1) lookup, its a set under the hood 

do the same thing 

"""



#! Problem 3: Navigating the research station 

"""
method 1:
increment using a nested loop and a count variable

method 2:
turn the first string into a dictionary for ele:index

for every char in str2:
add up the value if it exists 
    if it doesnt exist return err
return the total 
"""

#! Problem 4: Prioritizing endangered species observations 
#? hint mentions to look at extend in the cheatsheet but it is not even there 
"""
m1:
use the - ability to create a new list of elements not in lst2
append to end of lst2

m2:
iterate thru both lists in n^2
if in the first list, it does not exist in the second, append to end of second using extend function 
"""

#! Problem 5: Calculating Conservation Statistices 
"""
m1:
iterate until the list is empty 
store the min and max into variables 
get the average and store it into a list
pop both the max and the min values 
create a frequency map for teh aerage list 
create a new list and add only numbers with a frequency of 1 to it 
return the length of that new list

m2:
create a set to store the averages 
iterate and constantly add in the averages to the set
pop the min and max 
return the length of the set 
"""

# ! Problem 6: Wildfire re-introduction 

"""
m1:
great freq dictionaries of both strings 
iterate using a while loop
subtract from the frequency map while iterating through second string 
if a numbers frequency is zero, return the count variable 
once a loop finished, add 1 to the counter 
"""

string = "aaaaaabbbbccc"
from collections import Counter

newdict = Counter(string)
print(newdict)

#! Problem 7: Count Unique Species 
"""
eqweewqrqr
"""
#! Problem 8: Equivalent Species Pairs 
"""
get the frequency of pairs after normalizing 
iterate and use the equation to get the number of pairs 
"""