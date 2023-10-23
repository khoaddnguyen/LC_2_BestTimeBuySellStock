# given an array prices where prices[i] is stock price on i-th day
# 1 transaction mac per day, algo to find max profit, cannot sell before buy
# Input: prices = [7,1,5,3,6,4]
# Output: 5

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right = 0, 1  # left = buy, right = sell
        maxProfit = 0

        while right < len(prices):
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                maxProfit = max(maxProfit, profit)
            else:
                left = right
            right += 1

        return maxProfit



