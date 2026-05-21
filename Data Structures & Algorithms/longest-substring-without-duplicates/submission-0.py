class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # x y z y a b c -> zyabc
        window = set()
        maxLength = 0
        L = 0
        for R in range(len(s)):
            if s[R] in window:
                print("outside", L, window)
                while s[L] != s[R]:
                    window.remove(s[L])
                    L += 1
                    print("inside", L, window)
                window.remove(s[L])
                L += 1
            window.add(s[R])
            maxLength = max(maxLength, R-L+1)
        return maxLength



