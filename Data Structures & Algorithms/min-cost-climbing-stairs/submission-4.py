class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        total = 0

        plus_one = cost[-2]
        plus_two = cost[-1]
        for i in range(len(cost)-3, -1, -1):
            print(f"i: {i}, cost[i]: {cost[i]}, plus_one: {plus_one}, plus_two: {plus_two}" )
            curr = min(plus_one + cost[i], plus_two + cost[i])
            plus_two = plus_one
            plus_one = curr

        return min(plus_one, plus_two)


