class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # Fixed Sliding Window with set
        window = set()
        L = 0
        
        for R in range(len(nums)):
            # when R gets outside of the window we need to pull L to the right and fix the window
            if abs(L - R) > k: # Window size check
                window.remove(nums[L]) # what if the window contains multiple elements of the same number?
                L += 1
            if nums[R] in window:
                return True
            window.add(nums[R])

        return False