from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_s = defaultdict(lambda: 0)
        count_t = defaultdict(lambda: 0)

        for c in s:
            count_s[c] += 1
        for c in t:
            count_t[c] += 1

        return count_s == count_t