'''
Key with the Highest Value
Define a function which takes a dictionary as a parameter and returns the key with the highest value in a dictionary.

Example:

my_dict = {'a': 5, 'b': 9, 'c': 2}
max_value_key(my_dict))
Output:

b

'''

def max_value_key(my_dict):
    key,count = None,0
    for k,v in my_dict.items():
        if v > count:
            key,count = k,v
    return key

my_dict = {'a': 5, 'b': 9, 'c': 2}
print(max_value_key(my_dict))


'''
sol2: teacher sol
'''
def max_value_key2(my_dict):
    return max(my_dict, key=my_dict.get)
my_dict = {'a': 5, 'b': 9, 'c': 2}
print(max_value_key2(my_dict))
