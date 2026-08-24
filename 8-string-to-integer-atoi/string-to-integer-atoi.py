class Solution:
    def myAtoi(self, s: str) -> int:
        s=s.lstrip()
        l=[]
        sign=1
        m=0
        if s and (s[0]=="-" or s[0]=="+"):
            if s[0]=="-":
                sign=-1
            s=s[1:]
        for i in s:
            if i.isdigit():
                l.append(int(i))
            else:
                break
        for i in l:
            m*=10
            m+=i
        m*=sign
        if m<-2**31:
            return -2**31
        elif m>2**31-1:
            return 2**31-1
        else:
            return m


        
        