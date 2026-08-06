# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        newHead = ListNode(-1)
        tempNode = newHead
        while list1 and list2:
            if list1.val < list2.val:
                tempNode.next = list1
                list1 = list1.next
            else:
                tempNode.next = list2
                list2 = list2.next
            tempNode = tempNode.next
        
        while list1:
            tempNode.next = list1
            list1 = list1.next
            tempNode = tempNode.next

        while list2:
            tempNode.next = list2
            list2 = list2.next
            tempNode = tempNode.next

        
        return newHead.next
