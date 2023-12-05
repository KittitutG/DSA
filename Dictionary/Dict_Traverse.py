# traverse
'''
time comlexity O(N)
space comlexity O(1)
'''
myDict = {'Name':'Tae','Age':'25'}

def traverseDct(dct):
    for key in dct:
        print(key,dct[key])
traverseDct(myDict)