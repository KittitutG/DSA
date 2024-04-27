def CoinChange(totalNumber, coins):
    N = totalNumber
    coins.sort()
    index = len(coins) - 1
    while True:
        coinValue = coins[index]
        if N >= coinValue:
            N = N - coinValue
            print(coinValue)

        if  N < coinValue:
            index -=1

        if N ==0:
            break

coins =[1,3,5,50,100]
CoinChange(201,coins)