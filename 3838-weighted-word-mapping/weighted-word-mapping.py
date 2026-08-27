class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        ans=""
        for word in words:
            sm=0
            for let in word:
                lett=ord(let)-ord('a')
                sm+=weights[lett]
            rem=sm%26
            ans+=chr(122-rem)
        return ans

            
            
        
        
        