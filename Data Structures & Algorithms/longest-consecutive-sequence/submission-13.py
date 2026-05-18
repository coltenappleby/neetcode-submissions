class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        unique = set(nums)
        smalls = set()
        for num in unique:
            if num-1 in unique:
                continue
            smalls.add(num)

        output = 0
        for num in smalls:
            curr = 1
            output = max(output, curr)
            while curr < len(unique):
                num += 1
                if num in unique:
                    curr = curr + 1
                    output = max(output, curr)
                else:
                    break
        return output