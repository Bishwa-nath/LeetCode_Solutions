# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def dfs(node):
            if node is None:
                return []

            leaves = dfs(node.left) + dfs(node.right)
            return leaves or [node.val]

        return dfs(root1) == dfs(root2)
