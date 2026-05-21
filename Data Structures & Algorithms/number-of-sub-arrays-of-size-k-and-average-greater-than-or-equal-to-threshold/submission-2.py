class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        total = 0
        L = 0
        ans = 0

        # K SIZE

        for R in range(len(arr)):
            if R - L + 1 > k:
                total -= arr[L]
                L += 1

            total += arr[R]

            if total/k >= threshold and R-L+1== k:
                ans += 1
        return ans
            
    