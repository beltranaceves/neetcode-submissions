class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        nums_count = {}
        res = []
        for idx, num in enumerate(nums):
            if num > 0:
                break
            if idx > 0 and num == nums[idx - 1]:
                continue

            target = 0 - num
            l, r = idx + 1, len(nums) - 1
            while l < r:
                if nums[l] + nums[r] == target:
                    res.append([nums[idx], nums[l] , nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                elif nums[l] + nums[r] > target:
                    r -= 1
                else:
                    l += 1
        return res
