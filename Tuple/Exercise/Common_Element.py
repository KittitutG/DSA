'''

Common Elements
Write a function that takes two tuples and returns a tuple containing the common elements of the input tuples.

Example

tuple1 = (1, 2, 3, 4, 5)
tuple2 = (4, 5, 6, 7, 8)
output_tuple = common_elements(tuple1, tuple2)
print(output_tuple)  # Expected output: (4, 5)
'''
def common_elements(tuple1, tuple2):
    tup1 = set(list(tuple1))
    tup2 = set(list(tuple2))
    return tuple(tup1.intersection(tup2))

tuple1 = (1, 2, 3, 4, 5)
tuple2 = (4, 5, 6, 7, 8)
output_tuple = common_elements(tuple1, tuple2)
print(output_tuple)  # Expected output: (4, 5)

'''
sol2
'''
def common_elements2(tuple1, tuple2):
    return tuple(set(tuple1) & set(tuple2))
tuple1 = (1, 2, 3, 4, 5)
tuple2 = (4, 5, 6, 7, 8)
output_tuple = common_elements2(tuple1, tuple2)
print(output_tuple)  # Expected output: (4, 5)
