'''
Common Keys
Define a function with takes two dictionaries as parameters and merge them and sum the values of common keys.

Example:

dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 3, 'c': 4, 'd': 5}
merge_dicts(dict1, dict2)
Output:

{'a': 1, 'b': 5, 'c': 7, 'd': 5}
'''

def merge_dicts(dict1,dict2):
    dct ={}
    for i in dict1:
        dct[i] = dict1.get(i,0)
    for j in dict2:
        if j in dct.keys():
            dct[j] = dct[j] + dict2[j]
        else:
            dct[j] = dict2.get(j,0)
    return dct

dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 3, 'c': 4, 'd': 5}
print(merge_dicts(dict1, dict2))


'''
sol2: teacher solution
'''
def merge_dicts2(dict1, dict2):
    result = dict1.copy()
    for key, value in dict2.items():
        result[key] = result.get(key, 0) + value
    return result
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 3, 'c': 4, 'd': 5}
print(merge_dicts2(dict1, dict2))
