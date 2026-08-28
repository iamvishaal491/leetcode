class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        m={}
        n={}
        for i in s:
            if i not in m:
                m[i]=1
            m[i]+=1
        for j in t:
            if j not in n:
                n[j]=1
            n[j]+=1
        return m==n
        
        