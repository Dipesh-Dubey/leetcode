class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        win = defaultdict(int)
        maxie = 0
        for r in range(len(s)):
            win[s[r]] += 1
            while sum(win.values()) - max(win.values()) > k :
                win[s[l]] -= 1
                if  win[s[l]] == 0:
                    del win[s[l]]
                l += 1
            maxie = max(maxie,sum(win.values()))
        
        return maxie