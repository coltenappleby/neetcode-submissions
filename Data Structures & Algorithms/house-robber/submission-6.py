class Solution:
    def rob(self, nums: List[int]) -> int:
        # Brute Force
        # if len(nums)<=2:
        #     return nums[0]
        # option_1 = nums[0] + self.rob(nums[2:])
        # option_2 = self.rob(nums[1:])
        # if option_1 > option_2:
        #     return option_1
        # return option_2

        if len(nums) <=2:
            return max(nums)

        plus_two = nums[-1]
        plus_one = nums[-2]

        for i in range(len(nums)-3, -1, -1):
            curr = nums[i]
            best = max(plus_two + curr, plus_one)
            plus_two = plus_one
            plus_one = best

        return plus_one