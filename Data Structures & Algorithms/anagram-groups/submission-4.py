from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams_list = []

        for string in strs:
            # Build the anagram dicts
            new_anagram_dict = defaultdict(lambda: 0)
            for s in string:
                new_anagram_dict[s] += 1
            
            found_anagram = False
            for anagram_tuple in anagrams_list:
                anagram_dict, anagram_list = anagram_tuple
                if new_anagram_dict == anagram_dict:
                    anagram_list.append(string)
                    found_anagram = True
                    break
            if not found_anagram:
                anagrams_list.append((new_anagram_dict, [string]))

        anagrams_result = []
        for anagram_tuple in anagrams_list:
            _, anagram_list = anagram_tuple
            anagrams_result.append(anagram_list)
            
        return anagrams_result



