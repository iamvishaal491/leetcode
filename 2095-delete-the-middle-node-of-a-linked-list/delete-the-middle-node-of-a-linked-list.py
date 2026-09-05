# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(next=head)
        prev=dummy
        curr=head
        c=0
        while curr:
            curr=curr.next
            c+=1
        m=c//2
        for _ in range(m):
            prev=prev.next
        prev.next=prev.next.next
        return dummy.next