class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        window_start = minJump
        window_end = maxJump
        
        if s[-1] == '1':
            return False

        while window_end < len(s)-1:
            nws = None
            nwe = None
            for i in range(window_start, window_end+1):
                if s[i] == '1':
                    continue

                if nws is None:
                    nws = i+minJump
                    nwe = i+maxJump
                elif i + minJump <= nwe:
                    nws = max(nws,i)
                    nwe = i + maxJump

            if nws is None or nws > len(s)-1:
                return False
            else:
                window_start = nws
                window_end = nwe

        return True