class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False

        l = 0
        win = defaultdict(int)
        win1 = defaultdict(int)

        for s in s1:
            win1[s] += 1

        for r in range(len(s2)):
            win[s2[r]] += 1
            if sum(win.values()) == sum(win1.values()):
                if win == win1:
                    return True
                else:
                    win[s2[l]] -= 1
                    if win[s2[l]]==0:
                        del win[s2[l]] 
                    l+=1
        
        return False


