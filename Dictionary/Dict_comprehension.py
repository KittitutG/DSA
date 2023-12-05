import random
cityList = ['London','Paris','Tokyo','Beijing']

citytemp = {city:random.randint(20,30) for city in cityList}
print(citytemp)

tempGreater = {k:v for k,v in citytemp.items() if v >25}
print(tempGreater)