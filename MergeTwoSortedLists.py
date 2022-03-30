# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        newList = ListNode()
        start = newList
        while True:
            if newList == None or (list1 == None and list2 == None):
                break
            if list1 == None and list2 != None:
                newList.next = ListNode(list2.val, list2.next)
                break
            if list2 == None and list1 != None:
                newList.next = ListNode(list1.val, list1.next)
                break
            
            if list1.val < list2.val:
                newList.next = ListNode(list1.val)
                list1 = list1.next
                newList = newList.next
            elif list1.val > list2.val:
                newList.next = ListNode(list2.val)
                list2 = list2.next
                newList = newList.next
            else:
                newList.next = ListNode(list1.val, ListNode(list1.val))
                list1 = list1.next
                list2 = list2.next
                newList = newList.next.next
            self.printNodes(start)
            

        return start.next
    def printNodes(self, list1:Optional[ListNode]):
        while list1 != None:
            print(list1.val, "->", end=" ")
            list1 = list1.next
        print()