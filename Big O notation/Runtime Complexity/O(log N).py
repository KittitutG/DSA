'''
O(Log n) 
this will take Log N operation to complete the task.
eg. we have array of 1 - 10 and would like to find 1.
1,2,3,4,5,6,7,8,9,10

then we will divide them to two part
1,2,3,4 | 5, 6,7,8

as yo seen, 1 is on first half. so we will eliminate  second half


we will shrink number with this method again. so it should look like this
1,2 | 3,4 --> 1,2
1 | 2 --> 1
instead of us to travel 10 time. we only need 3 operation. to find number 1

eg. Log2 8 = 3

this will significantlyy useful when we dealt with big number 
eg. N =1048576
    log 2 1048576 = 20 
'''