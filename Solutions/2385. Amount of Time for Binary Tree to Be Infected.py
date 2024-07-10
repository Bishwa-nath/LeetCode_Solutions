# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        map = defaultdict(set)
        self.convert(root, 0, map)
        q = deque()
        q.append(start)
        minute = 0
        visited = set()
        visited.add(start)

        while q:
            level = len(q)
            while level > 0:
                curr = q.popleft()
                for n in map[curr]:
                    if n not in visited:
                        visited.add(n)
                        q.append(n)
                level -= 1
            minute += 1
        return minute - 1

    def convert(self, curr, parent, map):
        if not curr:
            return
        if curr.val not in map:
            map[curr.val] = set()

        adj_list = map[curr.val]
        if parent != 0:
            adj_list.add(parent)
        if curr.left:
            adj_list.add(curr.left.val)
        if curr.right:
            adj_list.add(curr.right.val)

        self.convert(curr.left, curr.val, map)
        self.convert(curr.right, curr.val, map)
