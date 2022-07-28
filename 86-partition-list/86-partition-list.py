# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        before = before_head = ListNode()
        after = after_head = ListNode()
        
        while head != None:
            if head.val < x:
                before.next = ListNode(head.val)
                before = before.next
            else:
                after.next = ListNode(head.val)
                after = after.next
            head = head.next
            
        before.next = after_head.next
        return before_head.next