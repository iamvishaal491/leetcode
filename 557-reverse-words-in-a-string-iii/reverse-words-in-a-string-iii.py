class Solution(object):
    def reverseWords(self, s):
        k= " ".join([words[::-1] for words in s.split(" ")])
        return k
        