from array import *

#1. Create an array and traverse.
print("Step 1")
my_array = array("i",[1,2,3,4,5])

for i in my_array:
    print(i) 

#2. Access element thorugh indexes
print("---------------------")
print("Step 2")
print(my_array[0])

#3. Append value using Append() method
print("---------------------")
print("Step 3")
my_array.append(6) #append() can only add element at the end of array
print(my_array)

#4. Insert value using insert() method
print("---------------------")
print("Step 4")
my_array.insert(0,11) #insert can add element at any given index
print(my_array)

#5. Extend value using extend() method
print("---------------------")
print("Step 5")
my_array1 = array("i",[10,11,12])
my_array.extend(my_array1) #extend can add another array to existing array
print(my_array)

#6. Add item from List using fromList() method
print("---------------------")
print("Step 6")
tempList = [20,21,22]
my_array.fromlist(tempList) #fromList() can add another list to existing array
print(my_array)

#7.Remove element using remove() method
print("---------------------")
print("Step 7")
my_array.remove(11) #remove() remove element from array on first encounter
print(my_array)

#8.Remove last element using pop() method
print("---------------------")
print("Step 8")
my_array.pop() #pop() remove last element from array
print(my_array)

#8.Remove last element using pop() method
print("---------------------")
print("Step 8")
my_array.pop() #pop() remove last element from array
print(my_array)

#9. find index position by using index() method
print("---------------------")
print("Step 9")
print(my_array.index(20)) #find index on given element


#10. Reverse array using reverse() method
print("---------------------")
print("Step 10")
my_array.reverse() #reversal array from back to start
print(my_array)

#11. Get array buffering information using buffer_info() method
print("---------------------")
print("Step 11")
print(my_array.buffer_info()) #buffer_info() get physical address and array size


#12. Check number of occurence using count() method
print("---------------------")
print("Step 12")
my_array.append(20)
print(my_array.count(20)) #count() get number of occurence on given data element


#13. Convert array to string using toString() method
## method is deprecated on python 3.9 and later
# print("---------------------")
# print("Step 12")
# strTMP = my_array.tostring()
# print(strTMP)
# print(type(strTMP))

#14. Convert array to list by using tolist()
print("---------------------")
print("Step 14")
print(my_array.tolist()) #toList() convert array to string

#15. Slice Element from array
print("---------------------")
print("Step 15")
print(my_array[1:4]) 

