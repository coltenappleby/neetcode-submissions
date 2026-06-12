class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)<2:
            return nums[0]
        
        plus_one, plus_two = max(nums[-2], nums[-1]), nums[-1]


        for i in range(len(nums)-3,-1,-1):
            best = max(nums[i] + plus_two, plus_one)
            plus_two = plus_one
            plus_one = best

        return plus_one