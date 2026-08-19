class Solution:
    def isPalindrome(self, n: int) -> bool:
        if(n<0):
            return False
        s=0
        m=n
        while(n!=0):
            r=n%10
            s=s*10+r
            n=n//10
        if (m==s):
            return True
        else:
            return False
        