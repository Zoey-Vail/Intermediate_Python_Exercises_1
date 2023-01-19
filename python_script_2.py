# Team members
# Ronnie Hampton
# Zoey Vail
# Michael
# Eli Huffman
# Quinn Harris

# Resources used: https://www.w3schools.com/python/python_dictionaries.asp

def get_combined_dict(dict1, dict2):
    combined_dict = dict()
    for i in dict1:
        for r in dict2:
            if i == r:
                combined_dict[i] =  (dict1[i] + dict2[r])
    return combined_dict

my_dict_1 = {'a': 5, 'b': 12, 'c': 3, 'd': 9}
my_dict_2 = {'b': 4, 'c': 9, 'd': 10, 'e': 16}
combined_dict = get_combined_dict(my_dict_1, my_dict_2)
print(combined_dict)