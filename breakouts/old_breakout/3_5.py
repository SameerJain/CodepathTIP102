
# Problem 1
"""
loop through the species_list 
track which dict has the lowest 
return the lowest 
"""
def most_endangered(species_list):
    min_val = float("inf")

    for i in range(len(species_list)):
        if species_list[i]["population"] < min_val:
            min_val = species_list[i]["population"]
            min_idx = i

    return species_list[min_idx]["name"]


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

# print(most_endangered(species_list))

# Problem 5 

def distinct_averages(species_populations):
    averages = set()
    while species_populations:
        min_val = min(species_populations) 
        max_val = max(species_populations)

        averages.add((min_val+max_val)/2)
        species_populations.remove(min_val)
        species_populations.remove(max_val)
    return len(averages)





species_populations1 = [4,1,4,0,3,5]
species_populations2 = [1,100]

print(distinct_averages(species_populations1))
print(distinct_averages(species_populations2)) 