class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1]
        postfix = [1]

        acum = 1
        for num in nums:
            prefix.append(acum*num)
            acum *= num

        acum = 1
        for idx in range(len(nums) - 1, -1, -1):
            postfix.append(acum*nums[idx])
            acum *= nums[idx]
        prefix.pop()
        postfix.pop()
        postfix.reverse()
        # print("prefix", prefix)
        # print("postfix", postfix)
        res = []
        for idx in range(0, len(nums)):
            res.append(prefix[idx]*postfix[idx])
        return res