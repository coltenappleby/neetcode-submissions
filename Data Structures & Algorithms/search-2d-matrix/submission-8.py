class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lasts = [row[-1] for row in matrix]

        # Find the lowest L

        L, R = 0, len(lasts)-1
        while L < R:
            mid = (R+L)//2

        #     if mid == 0:
        #         return binarySearch(matrix[0], target)
             
            if target <= lasts[mid]:
                R = mid
            if target > lasts[mid]:
                L = mid +1 
        return binarySearch(matrix[L], target)
            
def binarySearch(arr, target):
    L, R = 0, len(arr) - 1

    while L <= R:
        mid = (L + R) // 2

        if target > arr[mid]:
            L = mid + 1
        elif target < arr[mid]:
            R = mid - 1
        else:
            return True
    return False
