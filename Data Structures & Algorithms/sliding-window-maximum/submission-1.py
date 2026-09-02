class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []
        if len(nums) == k:
            return [max(nums)]
        window = nums[:k]
        r = k
        res = []
        while r < len(nums):
            res.append(max(window))
            window.pop(0)
            window.append(nums[r])
            r += 1
        res.append(max(window))
        print(f"window is {window} with k: {k}")
        return res