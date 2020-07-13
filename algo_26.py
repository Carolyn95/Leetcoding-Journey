# 19 remove Nth node from end of list
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        cur = head
        visited = []
        while cur:
            visited.append(cur)
            cur = cur.next
        length = len(visited)
        if n == length:
           head = head.next if head.next else None
        else:
            visited[length - n - 1].next = visited[length - n].next
            visited[length - n].next = None
        return head
