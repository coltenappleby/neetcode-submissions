class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        tot = 0
        length = len(nums)+1

        L = 0

        for R in range(len(nums)):
            tot += nums[R]

            while tot >= target:
                length = min(length, R-L+1)
                tot -= nums[L]
                L += 1
        return 0 if length == len(nums)+1 else length