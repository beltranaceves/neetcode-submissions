from collections import defaultdict
class Solution:
    def toCount(self, s: str):
        count = [0] * 26
        for c in s:
            idx = ord(c) - ord('a')
            count[idx] += 1
        return count

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        counts = defaultdict(lambda: [])
        for string in strs:
            count = self.toCount(string)
            counts[tuple(count)].append(string)

        return list(counts.values())