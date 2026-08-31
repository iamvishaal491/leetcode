# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        curr=head.next
        prev=head
        index=1
        num=[]
        while curr and curr.next:
            if curr.val> curr.next.val and curr.val> prev.val:
                num.append(index)
                
            elif curr.val<curr.next.val and curr.val<prev.val:
                num.append(index)
            prev=curr
            curr=curr.next
            
            index+=1
        if len(num)<2:
            return [-1,-1]
        min_d=float("inf")
        for i in range(1,len(num)):
            distance=num[i]-num[i-1]
            if distance<min_d:
                min_d=distance
        max_d=abs(num[-1]-num[0])
        return [min_d,max_d]
                


        