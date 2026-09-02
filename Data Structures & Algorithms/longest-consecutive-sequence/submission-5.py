class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        numS = set(nums)

        for num in nums:
            if (num - 1) not in numS:
                i = 0
                while (num + i) in numS:
                    i += 1
                res = max(res, i)

        return res

