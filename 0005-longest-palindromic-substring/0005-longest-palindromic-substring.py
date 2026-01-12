class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxie = 0
        res1,res2 = 0,0

        for i in range(len(s)):
            l = r = i
            while l>=0 and r<=len(s)-1 and s[l] == s[r]:
                if r-l+1 > maxie:
                    maxie = r-l+1
                    res1,res2 = l,r
                l -=1
                r += 1
            
            l,r = i,i+1
            while l>=0 and r<=len(s)-1 and s[l] == s[r]:
                if r-l+1 > maxie:
                    maxie = r-l+1
                    res1,res2 = l,r
                l -=1
                r += 1
        
        return s[res1:res2+1]
            