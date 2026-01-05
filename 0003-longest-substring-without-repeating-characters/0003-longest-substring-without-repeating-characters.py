class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        win = set()
        maxie = 0
        for r in range(len(s)):
            while s[r] in win:
                win.remove(s[l])
                l+=1                      
            win.add(s[r])
            maxie = max(maxie,r-l+1)
        return maxie

