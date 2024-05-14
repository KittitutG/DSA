'''
Given a list of number,
get the maximum sum of that list. but if you take one element , the nearby elements can not be picked
eg: [6,7,1,30,8,2,4]
option 1(take first element) = 6 + f(5) {skip 7}
option 2(skip first element) = f(6) {skip 6}
max(option1, option2) --> max(option N , option N+1)
'''

def houseRobber(houses, currentIndex):
    # base case to stop recursive call
    if currentIndex >= len(houses):
        return 0
    else:
        stealFirstHouse = houses[currentIndex] + houseRobber(houses, currentIndex+2)
        skipFirstHouse = houseRobber(houses, currentIndex+1)
        return max(stealFirstHouse,skipFirstHouse)

house = [6,7,1,30,8,2,4]
print(houseRobber(house,0))