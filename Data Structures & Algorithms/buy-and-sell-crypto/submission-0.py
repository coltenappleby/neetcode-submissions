class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        for B in range(len(prices)):
            for S in range(B, len(prices)):
                if prices[S] > prices[B]:
                    maxProfit = max(maxProfit, prices[S]-prices[B])
        return maxProfit