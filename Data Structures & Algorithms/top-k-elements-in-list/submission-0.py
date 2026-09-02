class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = {}
        for num in nums:
            if num in freqs:
                freqs[num] += 1
            else:
                freqs[num] = 1

        k_list = [[] for i in range(len(nums) + 1)]
        for key in freqs.keys():
            k_list[freqs[key]].append(key)
        res = []
        r = len(res) - 1
        while len(res) < k:
            if k_list[r]:
                res.append(k_list[r].pop())
            else:
                r -= 1
        return res


