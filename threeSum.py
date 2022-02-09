# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        answer = ListNode()
        first = answer
        carry = 0
        
        while True:
            if l1 == None and l2 == None:
                break
            a = 0
            if l1 != None:
                a = l1.val
                l1 = l1.next

            b = 0
            if l2 != None:
                b = l2.val
                l2 = l2.next
                
            answer.next = ListNode((a+b+carry) % 10)
            answer = answer.next
            carry = (a+b+carry) // 10

        if carry != 0:
            answer.next = ListNode(1)
        return first.next
