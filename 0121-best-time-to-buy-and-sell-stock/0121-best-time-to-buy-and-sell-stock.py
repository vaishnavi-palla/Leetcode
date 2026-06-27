class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini = prices[0]
        maxi = 0
        for price in prices[1:]:
            if price < mini:
                mini = price
            profit = price - mini
            if profit > maxi:
                maxi = profit
        return maxi