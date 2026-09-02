class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return 1
            
        res = 0
        curr = []

        for num in nums:
            curr.append(num)
            while curr and abs(max(curr) - min(curr)) > limit:
                curr.pop(0)
            res = max(res, len(curr))

        return res
