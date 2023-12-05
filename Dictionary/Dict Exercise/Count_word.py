'''
Count Word Frequency
Define a function to count the frequency of words in a given list of words.

Example:

words = ['apple', 'orange', 'banana', 'apple', 'orange', 'apple'] 
count_word_frequency(words) 
Output:

 {'apple': 3, 'orange': 2, 'banana': 1}
'''
def count_word(arr):
    dct = {}
    for i in arr:
        if i not in dct:
            dct[i] = 1
        else: 
            dct[i] = dct[i] + 1
    return dct
    
words = ['apple', 'orange', 'banana', 'apple', 'orange', 'apple'] 
print(count_word(words))


'''
sol 2: from teacher explanation
'''
def count_word_frequency(words):
    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    return word_count
print(count_word_frequency(words))
