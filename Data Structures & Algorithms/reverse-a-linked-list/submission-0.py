# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        dummy = ListNode(-1)
        while curr:
            if not dummy.next:
                dummy.next = ListNode(curr.val)
            else:
                temp = dummy.next
                dummy.next = ListNode(curr.val)
                dummy.next.next = temp
            curr = curr.next
        return dummy.next




        