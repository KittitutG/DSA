# delete
'''
time comlexity O(1) --> exceptional for clear() method
space comlexity O(1)
'''

'''
simply delete dict[key]
'''
myDict = {'Name':'Tae','Age':'25','City':'Bangkok'}

del myDict['Age']
print(myDict)


'''
pop out given dict key
'''
myDict = {'Name':'Tae','Age':'25','City':'Bangkok'}


removed_element = myDict.pop('Nam',None) #we should always set default value (2nd paramenter) to avoid Error to be raised
print(removed_element)
print(myDict)


'''
remove last key,value pair on dict
'''
myDict = {'Name':'Tae','Age':'25','City':'Bangkok'}

removed_element = myDict.popitem() #we should always set default value (2nd paramenter) to avoid Error to be raised
print(removed_element)
print(myDict)


'''
truncate dict and make dict empty again
this will take 
time colexity to O(n) since we need to traverse to each element
'''
myDict = {'Name':'Tae','Age':'25','City':'Bangkok'}

myDict.clear()
print(myDict)

