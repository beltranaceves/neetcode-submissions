# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = [(0, root)]
        res = []
        layer = 0
        while queue:
            lay, elem = queue.pop()
            if lay > len(res) - 1:
                res.append([])
            res[lay].append(elem.val)
            if elem.right:
                queue.append((lay + 1, elem.right))
            if elem.left:
                queue.append((lay + 1, elem.left))
            
        return res
