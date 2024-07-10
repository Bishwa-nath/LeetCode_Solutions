# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.res = []

    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        arr = ''
        if not root:
            return []
        self.getPath(root, arr)
        return self.res

    def getPath(self, node, arr):
        n_arr = arr + str(node.val)
        if not node.left and not node.right:
            self.res.append(n_arr)
            return
        else:
            n_arr += '->'
            if node.left:
                self.getPath(node.left, n_arr)
            if node.right:
                self.getPath(node.right, n_arr)

        return
