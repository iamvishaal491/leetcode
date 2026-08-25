class Solution:
    def removeDuplicates(self, st: str, k: int) -> str:
        s=[]
        for p in st:
            if (s) and (s[-1][0]==p):
                s[-1][1]=s[-1][1]+1
            else:
                s.append([p,1])
            if (s[-1][1]==k):
                s.pop()
        r=""
        for ch,c in s:
            r=r+ch*c
        return r


                

        