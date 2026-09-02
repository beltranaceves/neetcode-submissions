class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = {}

        for num in nums:
            if num in freqs:
                freqs[num] += 1
            else:
                freqs[num] = 0

        freq_list = [[] for i in range(len(nums) + 1)]
        for key in freqs.keys():
            freq_list[freqs[key]].append(key)

        r = len(nums) - 1
        top_k = []
        while len(top_k) < k:
            if freq_list[r]:
                top_k.append(freq_list[r].pop())
            else:
                r -= 1

        return top_k
        
    
