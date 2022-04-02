from typing import Optional
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = head
        while prev != None and prev.next != None:
            if prev.val == prev.next.val:
                prev.next = prev.next.next
            else:
                prev = prev.next
        return head