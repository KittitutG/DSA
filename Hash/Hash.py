'''
Hash function should be able to distribute data unifomely and avoid any collision
example:
Hash int input: using mod(input % hash_table_size)
     string input: convert string to ASCII and using mod(input % hash_table_size)


Collision handle:
case 1: direct chaining --> store hash value as linked list 
case 2: opend addressing --> store hash value on next non-empty cell
case 3: quadratic addressing --> store hash value on next non-empty cell by jumping with avrbitary index(eg. 1+n**2)
case 4: double hashign --> interval between probes is computed by another hash function (hash over hash when collision happen)
'''