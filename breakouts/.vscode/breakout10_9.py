
# def extract_nft_names(nft_collection):
#     nft_names = []
#     for nft in nft_collection:
#         nft_names.append(nft["name"])
#     return nft_names

# nft_collection = [
#     {"name": "Abstract Horizon", "creator": "ArtByAlex", "value": 5.4},
#     {"name": "Pixel Dreams", "creator": "DreamyPixel", "value": 7.2}
# ]

# nft_collection_2 = [
#     {"name": "Golden Hour", "creator": "SunsetArtist", "value": 8.9}
# ]

# nft_collection_3 = []

# print(extract_nft_names(nft_collection))
# print(extract_nft_names(nft_collection_2))
# print(extract_nft_names(nft_collection_3))

"""
U- return the list of the names of the popular creators 
P- get the frequency of all creators in the collection 
use a hashmap (dictionary) to store the values 
return a value more than 1 if it exists else return none 

I-
"""

def identify_popular_creators(nft_collection):
    freqs = {}
    result = []

    for artist in nft_collection:
        creator = artist['creator']
        freqs[creator] = freqs.get(creator,0) + 1

    for key, value in freqs.items():
        if value > 1:
            
            result.append[str(key)]

    return result 

def identify_popular_creators0(nft_collection):
    result = []
    result2 = []
    for nft in nft_collection:
        if nft['creator'] not in result:
            result.append(nft['creator'])
        else:
            result2.append(nft['creator'])
    return result2

nft_collection = [
    {"name": "Abstract Horizon", "creator": "ArtByAlex", "value": 5.4},
    {"name": "Pixel Dreams", "creator": "DreamyPixel", "value": 7.2},
    {"name": "Urban Jungle", "creator": "ArtByAlex", "value": 4.5}
]

nft_collection_2 = [
    {"name": "Crypto Kitty", "creator": "CryptoPets", "value": 10.5},
    {"name": "Galactic Voyage", "creator": "SpaceArt", "value": 6.7},
    {"name": "Future Galaxy", "creator": "SpaceArt", "value": 8.3}
]

nft_collection_3 = [
    {"name": "Golden Hour", "creator": "SunsetArtist", "value": 8.9}
]

print(identify_popular_creators(nft_collection))
print(identify_popular_creators(nft_collection_2))
print(identify_popular_creators(nft_collection_3))