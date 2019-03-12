# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        l_node = self.maxDepth(root.left)
        r_node = self.maxDepth(root.right)
        return max(l_node, r_node)+1
