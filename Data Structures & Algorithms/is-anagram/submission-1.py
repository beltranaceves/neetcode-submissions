from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        charCount1 = {}
        charCount2 = {}
        for character in s:
            if character in charCount1:
                charCount1[character] += 1
            else:
                charCount1[character] = 1

        for character in t:
            if character in charCount2:
                charCount2[character] += 1
            else:
                charCount2[character] = 1
        
        
        return charCount1 == charCount2