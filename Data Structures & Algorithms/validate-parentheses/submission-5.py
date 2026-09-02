class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        opposites = {
            "(": ")",
            "[": "]",
            "{": "}",
        }
        for token in s:
            if token in ["(", "{", "["]:
                stack.append(token)
            elif not stack:
                return False
            elif token == opposites[stack[-1]]:
                stack.pop(-1)
            else:
                return False

        return len(stack) == 0
