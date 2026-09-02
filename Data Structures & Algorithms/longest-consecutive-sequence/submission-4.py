class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        exists = set()

        longest = 0

        for num in nums:
            exists.add(num)
        
        for num in exists:
            print(num, exists)
            if (num - 1) not in exists:
                count = 1
                while (num + count) in exists:
                        count += 1
                longest = max(longest, count)

        return longest


