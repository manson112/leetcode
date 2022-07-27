# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        tail = head
        length = 1
        while tail.next != None:
            tail = tail.next
            length += 1
        
        if length == 1:
            return head
        
        if length < k:
            length = length * (k // length + 1)
        
        k = length - k
        
        for _ in range(k):
            tail.next = head
            head = head.next
            tail.next.next = None
            tail = tail.next
        
        return head
        
        