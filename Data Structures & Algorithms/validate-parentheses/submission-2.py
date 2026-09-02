class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        opening = set("({[")
        closing = set("]})")
        back = {
            "]": "[",
            "}": "{",
            ")": "("
        }

        for element in s:
            if element in opening:
                stack.append(element)
            else:
                if not stack:
                    return False
                prev = stack.pop()
                if back[element] != prev:
                    return False
        return len(stack) == 0
