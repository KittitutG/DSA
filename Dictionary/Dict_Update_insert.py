# update
'''
time comlexity O(1)
space comlexity O(1)
'''
myDict = {'Name':'Tae','Age':'25'}
myDict['Name'] = 'Kittitut'
print(myDict)

# insert
'''
time comlexity O(1)
space comlexity Amotized O(1)
Amotized O(1): When they typically O(1) most of the time. but infrequently be O(N) when data growth/shrink
'''
myDict['City'] = 'Bangkok'
print(myDict)