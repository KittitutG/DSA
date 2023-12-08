'''

Elementwise Sum
Create a function that takes two tuples and returns a tuple containing the element-wise sum of the input tuples.

Example

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
output_tuple = tuple_elementwise_sum(tuple1, tuple2)
print(output_tuple)  # Expected output: (5, 7, 9)
'''
def tuple_elementwise_sum(tuple1, tuple2):
    tmp = [1]*len(tuple1)
    for i in range(0,len(tuple1)):
        tmp[i] = tuple1[i] + tuple2[i]
    return tuple(tmp)

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
output_tuple = tuple_elementwise_sum(tuple1, tuple2)
print(output_tuple)

'''
sol2
'''
def tuple_elementwise_sum2(t1, t2):
    if len(t1) != len(t2):
        raise ValueError("Input tuples must have the same length.")
 
    result = tuple(a + b for a, b in zip(t1, t2))
    return result
output_tuple = tuple_elementwise_sum2(tuple1, tuple2)
print(output_tuple)

'''
sol3
'''
def tuple_elementwise_sum3(tuple1, tuple2):
    return tuple(map(sum, zip(tuple1, tuple2)))
output_tuple = tuple_elementwise_sum3(tuple1, tuple2)
print(output_tuple)

