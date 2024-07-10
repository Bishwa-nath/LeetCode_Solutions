# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        self.diff = 0
        self.helper(root, root.val, root.val)
        return self.diff

    def helper(self, root, mn, mx):
        if not root:
            return
        self.diff = max(self.diff, max(abs(mn - root.val), abs(mx - root.val)))
        mn = min(mn, root.val)
        mx = max(mx, root.val)
        self.helper(root.left, mn, mx)
        self.helper(root.right, mn, mx)
