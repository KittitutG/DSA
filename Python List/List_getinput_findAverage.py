total = []
while(True):
    inp = input('Enter a number: ')
    if inp =='done': break
    value = float(inp)
    total.append(value) #accumulater input to list
    
average = sum(total) / len(total) #find average by sum/size

print('Average: ',average)