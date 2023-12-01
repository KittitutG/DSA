'''
convert string to list
'''
a = 'spam'
b = list(a)
print(b)


print('------------')
#split - get each string from string
a = 'spam-spam2-spam3'
print(a)
delimeter = '-'
b = a.split(delimeter)
print(b)

#joint -- conjunct given list with string to create new string
z = delimeter.join(b)
print(z)