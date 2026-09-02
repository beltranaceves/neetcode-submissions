# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        queue_root = [root]
        while queue_root:
            print("merry go round")
            root_node = queue_root.pop(-1)
            if not root_node:
                continue
            elif root_node.val == subRoot.val:
                if self.isSameTree(root_node, subRoot):
                    return True
            
            queue_root.append(root_node.left)
            queue_root.append(root_node.right)
        return False

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        queue_p = [p]
        queue_q = [q]
        
        while queue_p and queue_q:
            node_a = queue_p.pop(-1)
            node_b = queue_q.pop(-1)
            if  node_a and node_b and node_a.val == node_b.val:
                queue_p.append(node_a.left)
                queue_p.append(node_a.right)
                queue_q.append(node_b.left)
                queue_q.append(node_b.right)
            elif not node_a and not node_b:
                continue
            else:
                return False
        return True