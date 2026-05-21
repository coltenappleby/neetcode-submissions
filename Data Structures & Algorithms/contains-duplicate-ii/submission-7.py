class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # Fixed Sliding Window with set
        window = set()
        L = 0
        
        while R < len(nums):
            # when R gets outside of the window we need to pull L to the right and fix the window
            if R + L - 1 > k: # Window size check
                window.remove(nums[L]) # what if the window contains multiple elements of the same number?
                L += 1
            if nums[R] in window:
                return True
        return False