class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        window = []
        L = 0

        ans = 0

        # K SIZE

        for R in range(len(arr)):
            if R - L + 1 > k:
                window.remove(arr[L])
                L += 1

            window.append(arr[R])

            if sum(window)/len(window) >= threshold and len(window) == k:
                # print(window , sum(window)/len(window),sum(window)/len(window) >= threshold )
                ans += 1
        return ans
            
        


