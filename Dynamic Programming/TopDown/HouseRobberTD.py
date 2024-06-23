def houseRobberTD(house, currentIndex, tempDict):
    if currentIndex >= len(house):
        return 0
    else:
        if currentIndex not in tempDict:
            stealHouse = house[currentIndex] + houseRobberTD(house, currentIndex+2, tempDict)
            skipHouse = houseRobberTD(house, currentIndex+1, tempDict)
            tempDict[currentIndex] = max(stealHouse , skipHouse)
        return tempDict[currentIndex]
    
house = [6,7,1,30,8,2,4]
print(houseRobberTD(house,0,{}))