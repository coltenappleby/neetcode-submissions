class Solution:
    def climbStairs(self, n: int) -> int:
        def memoization(n, cache):
            if n in cache:
                return cache[n]
            if n == 0:
                return 1
            if n < 0:
                return 0
            cache[n] = memoization(n-1, cache) + memoization(n-2, cache)

            return cache[n]
        return memoization(n, {})

