class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for num in nums]
        counts = {}

        for num in nums:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1
        
        for key in counts.keys():
            freq = counts[key]
            buckets[freq - 1].append(key)
        
        counter = 0
        r = len(buckets) - 1
        res = []

        while counter < k:
            if buckets[r] != []:
                res.append(buckets[r].pop())
                counter += 1
            else:
                r -= 1
        return res

