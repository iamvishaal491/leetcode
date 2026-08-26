class Solution:
    def isValid(self, s: str) -> bool:
        stk=[]
        d={')':'(','}':'{',']':'['}
        for c in s:
            if c not in d:
                stk.append(c)
            else:
                if not stk:
                    return False
                else:
                    popped=stk.pop()
                    if popped !=d[c]:
                        return False
        return stk==[]


            
        