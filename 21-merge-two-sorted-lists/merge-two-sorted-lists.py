# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode()
        prev=dummy
        curr1=list1
        curr2=list2
        while curr1 and curr2:
            if curr1.val<curr2.val:
                prev.next=curr1
                curr1=curr1.next
            else:
                prev.next=curr2
                curr2=curr2.next
            prev=prev.next
        if curr1:
            prev.next=curr1
        else:
            prev.next=curr2
        return dummy.next
        