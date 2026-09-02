class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = []
        def backtracking(openP, closeP):
            # print("stack: ", stack)
            if openP == n and closeP == n and stack[-1] == ")":
                res.append("".join(stack))

            if openP < closeP:
                return

            if openP < n:
                stack.append("(")
                backtracking(openP + 1, closeP)
                stack.pop()
            
            if closeP < n:
                stack.append(")")
                backtracking(openP, closeP + 1)
                stack.pop()

        backtracking(0, 0)
        return res