class Solution:
    def beautySum(self, s: str) -> int:
        n,ans = len(s),0

        for i in range(n):
            freq = defaultdict(int)
            for j in range(i,n):
                freq[s[j]] += 1

                maxFreq = max(freq.values())
                minFreq = min(freq.values())

                ans += maxFreq - minFreq

        return ans
                
            