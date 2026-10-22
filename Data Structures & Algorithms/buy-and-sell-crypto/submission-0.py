class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1
        result = 0

        while right < len(prices):
            if prices[left] < prices[right]:
                result = max(result, prices[right] - prices[left])
            else:
                left = right
            right += 1

        return result