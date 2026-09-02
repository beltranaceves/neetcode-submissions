class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        l, r = 0, 1

        res = nums[l]
        curr = 0
        for n in nums:
            if curr < 0:
                curr = 0
            curr += n
            res = max(curr, res)
            
        return res