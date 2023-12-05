# linear search
'''
time comlexity O(N)
space comlexity O(1)
'''
myDict = {'Name':'Tae','Age':'25','City':'Bangkok'}

def searchDict(dct,target):
    for key in dct:
        if dct[key] == target:
            return key, target
    return 'Element not found'

print(searchDict(myDict,'25'))