class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        deltas = {}
        for i in range(len(nums)):
            delta = target - nums[i]
            if delta in deltas:
                return [deltas[delta], i]
            deltas[nums[i]] = i