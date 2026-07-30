class Solution:
    def maxDepth(self, s: str) -> int:
        counter = 0
        maxie = 0

        for c in s:
            if c == "(": counter+=1
            if c == ")": counter-=1

            maxie = max(maxie,counter)
        
        return maxie