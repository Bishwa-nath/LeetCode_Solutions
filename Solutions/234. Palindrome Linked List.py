# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        ls = []
        while head:
            ls.append(head.val)
            head = head.next

        st = ''.join(map(str, ls))
        return st == st[::-1]