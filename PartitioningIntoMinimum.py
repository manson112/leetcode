# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode()
        resultHead = result
        tSum = 0
        head = head.next
        while head:
            if head.val == 0:
                result.next = ListNode(tSum)
                result = result.next
                tSum = 0
            else:
                tSum += head.val
            
            head = head.next
        return resultHead.next