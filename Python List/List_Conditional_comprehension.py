# prev_lst = [1,2,3,10,20,30]
# new_lst = [item for item in prev_lst if item>=10]
# print(prev_lst)
# print(new_lst)


# square_lst = [item*item for item in prev_lst if item>=10]
# print(square_lst)

'''
function inside list comprehension
'''
sentence = 'My name is Kittitut'

def is_consonant(sentence):
    voewl = 'aeiou'
    return sentence.isalpha() and sentence.lower() not in voewl
consonant = [i for i in sentence if is_consonant(i)]
print(consonant)


'''
Condition on expression
'''
prev_lst = [1,20,3,50,3,40]
new_lst = [item if item >= 10 else 'This is lower than 10' for item in prev_lst]
print(prev_lst)
print(new_lst)

