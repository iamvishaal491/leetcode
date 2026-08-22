# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy=ListNode(next=head)
        prev=dummy
        curr=head
        c=0
        while curr:
            curr=curr.next
            c+=1
        for i in range(c-n):
            prev=prev.next
        prev.next=prev.next.next
        return dummy.next

        
        