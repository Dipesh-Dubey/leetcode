class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s

        maxie = 0
        res1,res2 = -1,-1

        for i,c in enumerate(s):
            l = i-1
            r = i+1
            while r<=len(s)-1 and c == s[r]:
                r += 1
                if maxie < r-l-1:
                    maxie = r-l-1
                    res1,res2 = l+1,r-1
            while l!=-1 and r<=len(s)-1 and s[l] == s[r]:
                if r-l+1 > maxie:
                    maxie = r-l+1
                    res1,res2 = l,r                   
                l -= 1
                r += 1

        return s[res1:res2+1] if res1 != -1 else s[0]
            