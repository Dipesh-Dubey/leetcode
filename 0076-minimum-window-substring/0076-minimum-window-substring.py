class Solution:
    def minWindow(self, s: str, t: str) -> str:
        minie = float('inf')
        l = 0
        win = defaultdict(int)
        comp = defaultdict(int)

        for i in range(len(t)):
            comp[t[i]] += 1
        unique = len(comp)
        count = 0

        res1,res2 = -1,-1
        for r in range(len(s)):
            win[s[r]] += 1

            if s[r] in comp and comp[s[r]]==win[s[r]]:
                count += 1

            while unique==count:
                if r-l+1 < minie:
                    minie = r-l+1
                    res1,res2 = l,r

                win[s[l]] -= 1              
                if s[l] in comp and win[s[l]] < comp[s[l]]:
                    count -= 1

                if win[s[l]] == 0:
                    del win[s[l]]  

                l+=1

        return "" if res1==-1 else s[res1:res2+1]

        