class Solution(object):
    def lengthOfLastWord(self, s):
        m=s.split()
        k=list(m[-1])
        return len(k)