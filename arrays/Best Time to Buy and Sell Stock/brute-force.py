def maxProfit(self, prices):
    n=len(prices)
    max_profit=0
    for i in range(0,n):
        for j in range(i+1,n):
            if prices[j]>prices[i]:
             profit=prices[j]-prices[i]
             max_profit=max(max_profit,profit)
    return max_profit
                  