# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        target = None
        leftEndOfTarget = None
        befoLeftEnd = None
        fakeHead = ListNode(-1, head)
        befo = fakeHead
        temp = head
        
        while temp != None:
            if leftEndOfTarget == None and temp.val >= x:
                leftEndOfTarget = temp
                befoLeftEnd = befo
            if temp.val == x:
                target = temp
            if temp.val < x:
                if befoLeftEnd != None:
                    befo.next = temp.next
                    befoLeftEnd.next = temp
                    temp.next = leftEndOfTarget
                    befoLeftEnd = temp
                    temp = befo.next
                    continue
            befo = temp
            temp = temp.next
        return fakeHead.next