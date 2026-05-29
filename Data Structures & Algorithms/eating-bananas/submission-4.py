import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # binary search
        low = 1
        high = max(piles) + 1
        
        while low < high:
            mid = (high + low)//2
            tot = 0
            for pile in piles:
                tot += math.ceil(pile/mid)
            if tot <= h:
                high = mid
            else:
                low = mid + 1
        return high
            
            