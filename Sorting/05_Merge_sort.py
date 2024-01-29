'''
divide data into smaller chnk until atomic. then merger them back in order(sort)

time : O(NlogN)
space: O(N)

when to use:
    -stable sort
    -average time is O(NlogN)
when to avoid
    -space is concern
'''

def merge(customList, l ,m ,r):
    n1 = m - l + 1 #first half index
    n2 = r - m #second half index

    L = [0] *(n1) #first array size
    R = [0] *(n2) #second array size

    for i in range(0, n1):
        L[i] = customList[l+i] #put data into first half
        
    for j in range(0, n2):
        R[j] = customList[m+1+j] #put data into first half

    i = j = 0
    k=l #index pointer

    #merge 
    while i< n1 and j < n2:
        if L[i] <= R[j]:
            customList[k] = L[i]
            i+=1
        else:
            customList[k] = R[j]
            j+=1
        k+=1

    #leftover from first half
    while i < n1:
        customList[k] = L[i]
        i+=1
        k+=1

    #leftover from first half
    while j < n2:
        customList[k] = R[j]
        j+=1
        k+=1


def mergeSort(customList,l,r):
    if l < r:
        m = (l + (r-1))//2
        mergeSort(customList, l ,m)
        mergeSort(customList,m+1,r)
        merge(customList,l,m,r)

    return customList

my_list = [5,10,9,6,7,2]
print(mergeSort(my_list,0,5))