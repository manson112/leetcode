from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        result = None

        s = set()
        tA = headA
        tB = headB
        while tA:
            s.add(tA)
            tA = tA.next
        while tB:
            bef = len(s)
            s.add(tB)
            af = len(s)
            if bef == af:
                result = tB
                break
            tB = tB.next

        return result

print("{}".format())