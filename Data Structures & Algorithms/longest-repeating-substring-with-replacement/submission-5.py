class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        letters = {}
        L = 0
        output = 0
        for R  in range(len(s)):
            letters[s[R]] = letters.get(s[R], 0) + 1

            while R-L+1 - max(letters.values()) > k:
                letters[s[L]] -= 1
                L += 1
            output = max(output, R-L+1)
        return output