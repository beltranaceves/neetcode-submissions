from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letters_s = defaultdict(lambda: 0)
        letters_t = defaultdict(lambda: 0)

        for letter in s:
            letters_s[letter] += 1

        for letter in t:
            letters_t[letter] += 1

        return letters_s == letters_t