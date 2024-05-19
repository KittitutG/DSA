def findLPS(s ,start, stop):
    if start > stop:
        return 0
    elif start == stop:
        return 1
    
    # hit
    elif s[start] == s[stop]:
        return 2 +findLPS(s, start+1,stop-1)
    # miss
    else:
        op1 = findLPS(s, start, stop-1)
        op2 = findLPS(s, start+1, stop)
        return max(op1, op2)

print(findLPS("ELRMENMET", 0, 8))