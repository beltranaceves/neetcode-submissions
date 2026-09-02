# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def depth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + max(self.depth(root.left), self.depth(root.right))

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        l_depth = self.depth(root.left)
        r_depth = self.depth(root.right)
        if abs(l_depth - r_depth) < 2:
            l_balance = self.isBalanced(root.left)
            r_balance = self.isBalanced(root.right)
            return l_balance and r_balance
        else:
            return False