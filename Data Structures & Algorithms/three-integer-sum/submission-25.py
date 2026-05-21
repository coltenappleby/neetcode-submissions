class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        
        for L in range(len(nums)):
            M = L + 1
            R = len(nums)-1

            if L != 0 and nums[L] == nums[L-1]:
                continue

            while M < R:
                if nums[M] + nums[R] + nums[L] > 0:
                    R -= 1
                    while nums[R] == nums[R+1] and M < R:
                        R-=1
                elif nums[M] + nums[R] + nums[L] < 0:
                    M += 1
                    while nums[M] == nums[M-1] and M < R:
                        M += 1
                else:
                    ans.append([nums[L], nums[M], nums[R]])
                    R -= 1
                    M += 1
                    while nums[M] == nums[M-1] and M < R:
                        M += 1
                    while nums[R] == nums[R+1] and M < R:
                        R-=1
        return ans
