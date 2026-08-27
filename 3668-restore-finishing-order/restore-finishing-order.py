class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        stk=[]
        for i in order:
            if i in friends:
                stk.append(i) 
        return stk
        