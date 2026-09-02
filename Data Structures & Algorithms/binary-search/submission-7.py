class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        if len(nums) == 1:
            return 0 if nums[0] == target else -1

        l, r = 0, len(nums) - 1
        while 1:
            mid = (r + l) // 2
            if l == r or l >= r:
                return -1
            if nums[l] == target:
                return l
            if nums[r] == target:
                return r
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid - 1
            else:
                # nums[mid] < target
                l = mid + 1
