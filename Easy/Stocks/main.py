
def maxProfit(prices):
    if not prices:
        return 0

    min_price = prices[0]
    max_profit = 0

    for price in prices[1:]:
        profit = price - min_price
        if profit > max_profit:
            max_profit = profit
        if price < min_price:
            min_price = price

    return max_profit

#Pomalé moc
""" def maxProfit(prices):
    
    :type prices: List[int]
    :rtype: int
   
    ans=0
    for i in range(len(prices)):
        for l in range(i,len(prices)):
            if -prices[i]+prices[l]>ans:
                ans = -prices[i]+prices[l]
    return ans """





prices = [7,1,5,3,6,4]

print(maxProfit(prices))