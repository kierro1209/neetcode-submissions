class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        current_buy = prices[0]
        current_sell = 0
        start = 0
        max_profit = -100
        for i in range(1,len(prices)):
            profit = prices[i] - min(prices[0:i])
            if profit > max_profit:
                max_profit = profit
            
        
        if max_profit < 0:
            return 0
        return max_profit
                

        