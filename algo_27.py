# 234 palindrome linked list
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        vals = []
        cur = head
        while cur:
            vals.append(cur.val)
            cur = cur.next
        return vals == vals[::-1]
