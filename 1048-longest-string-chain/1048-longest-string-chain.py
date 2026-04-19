class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        n = len(words)
        dp = [1]*n
        def comp(w1, w2):
            if len(w2) - len(w1) != 1:
                return False
            i = j = 0
            mismatch = 0      
            while i < len(w1) and j < len(w2):
                if w1[i] == w2[j]:
                    i += 1
                    j += 1
                else:
                    mismatch += 1
                    j += 1
                    if mismatch > 1:
                        return False       
            return True
        words.sort(key=len)
        for ind in range(n):
            for prev_ind in range(ind):
                if comp(words[prev_ind],words[ind]):
                    if dp[prev_ind]+1 > dp[ind]:
                        dp[ind] = dp[prev_ind]+1
        
        maxi = 0
        for i in range(n):
            if dp[i]>maxi: 
                maxi = dp[i]
        
        return maxi

