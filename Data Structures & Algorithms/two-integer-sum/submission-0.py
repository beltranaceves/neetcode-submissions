class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        memory = {}

        for idx, num in enumerate(nums):
            offset = target - num
            if offset in memory:
                return [memory[offset], idx]
            else:
                memory[num] = idx