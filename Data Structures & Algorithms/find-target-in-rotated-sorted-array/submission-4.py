class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1


        while left < right:
            mid = (left+right)//2
            if nums[mid] == target:
                return mid

            if nums[mid] < nums[right]:
                right = mid
            else:
                left = mid+1
            
        pivot = left
        print("pivot:", pivot)

        if target == nums[pivot]:
            return pivot
        if target > nums[pivot] and target <= nums[len(nums)-1]:
            left, right = pivot+1, len(nums)-1
        else:
            left, right = 0, pivot-1

        print("left:", left, "right:", right)

        while left <= right:
            mid = (left+right)//2
            if target == nums[mid]:
                return mid
            if target < nums[mid]:
                right = mid-1
            else:
                left = mid+1
        return -1






# Option (1) Find the pivot and iterate from there
# Option (2) Binary search to find the pivot, then binary search to find the value