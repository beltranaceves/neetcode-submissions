# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        furthest = [0]
        if not root:
            return 0

        def drillSides(root: Optional[TreeNode], currentDepth: int) -> None:
            if root:
                furthest[0] = max(currentDepth + 1, furthest[0])
                drillSides(root.left, currentDepth + 1)
                drillSides(root.right, currentDepth + 1)        
            return None

        if root.left:
            drillSides(root.left, 0)
        if root.right:
            drillSides(root.right, 0)

        return furthest[0]+1