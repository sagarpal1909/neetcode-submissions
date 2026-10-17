class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        mini = prices[0]
        best = 0

        for price in prices[1:]:
            best = max(best, price - mini)
            mini = min(mini, price)

        return best
        