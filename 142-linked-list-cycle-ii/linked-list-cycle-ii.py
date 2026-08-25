class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        c=0
        slow=fast=head
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
            if slow==fast:
                slow=head
                while slow!=fast:
                    fast=fast.next
                    slow=slow.next
                return slow
        return None 