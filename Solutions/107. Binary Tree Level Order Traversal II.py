# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        Q = deque([root])
        levels = [[root.val]]
        temp = deque()

        while Q:
            node = Q.popleft()
            if node.left:
                temp.append(node.left)
            if node.right:
                temp.append(node.right)
            if not Q:
                if temp:
                    levels.append([t.val for t in temp])
                Q = temp
                temp = deque()

        ans = []
        while levels:
            ans.append(levels.pop())
        return ans
