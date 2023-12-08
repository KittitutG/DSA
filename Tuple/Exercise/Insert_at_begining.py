'''
Insert at the Beginning
Write a function that takes a tuple and a value, and returns a new tuple with the value inserted at the beginning of the original tuple.

Example

input_tuple = (2, 3, 4)
value_to_insert = 1
output_tuple = insert_value_front(input_tuple, value_to_insert)
print(output_tuple)  # Expected output: (1, 2, 3, 4)
'''
def insert_value_front(input_tuple, value_to_insert):
    tmp = [1]*(len(input_tuple)+1)
    tmp[0] = value_to_insert
    print(tmp)
    for i in range(0,len(input_tuple)):
        tmp[i+1] = input_tuple[i]
    return tuple(tmp)

input_tuple = (2, 3, 4)
value_to_insert = 1
output_tuple = insert_value_front(input_tuple, value_to_insert)
print(output_tuple)  # Expected output: (1, 2, 3, 4)


'''
sol2
'''
def insert_value_front2(input_tuple, value_to_insert):
    return (value_to_insert,) + input_tuple
input_tuple = (2, 3, 4)
value_to_insert = 1
output_tuple = insert_value_front2(input_tuple, value_to_insert)
print(output_tuple)  # Expected output: (1, 2, 3, 4)

