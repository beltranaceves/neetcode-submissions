class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Step 1: preprocess the string to only contain alfanumeric values
        pp_s = "".join([character.lower() for character in s if character.isalnum()])
        # Step 2: Use two l and r pointers to check the symmetry
        l, r = 0, len(pp_s) - 1

        while l < r:
            if pp_s[l] != pp_s[r]:
                return False

            l += 1
            r -= 1
        return True