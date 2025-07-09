def stocks(prices):
    min_price=float('inf')
    max_price=0

    for price in prices:
        if price<min_price:
            min_price=price
        else:
            profit=price-min_price
            max_price=max(max_price,profit)
    return max_price

prices=list(map(int,input("enter the array number:").split()))
result=stocks(prices)
print(result)


enter the array number:4 5 1 2 3
2
