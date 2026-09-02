class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []
        nums.sort()

        if len(nums) == 3:
            if sum(nums) == 0:
                return [nums]
            else:
                return []

        for idx, num in enumerate(nums):
            if idx > 0 and nums[idx] == nums[idx-1]:
                continue

            l, r = idx + 1, len(nums) - 1

            while l < r:
                triplet = num + nums[l] + nums[r]
                if triplet == 0:
                    triplets.append([num, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l-1] and l < r:
                        l+=1
                elif triplet < 0:
                    l += 1
                elif triplet > 0:
                    r -= 1

        return triplets