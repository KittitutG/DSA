
numberOfDays = int(input('please enter number: '))
total = 0
lst= []
for i in range(numberOfDays+1):
    tempDay = float(input(f'What is day {i+1} hight temp of this day: '))
    lst.append(tempDay)
    total =+ lst[i]
avg = round(total/numberOfDays,2)
print("\nAverage Number: ",avg)
count_above = len([item for item in lst if item > avg])
print(f"there's' {count_above} days(s) above average temparature")