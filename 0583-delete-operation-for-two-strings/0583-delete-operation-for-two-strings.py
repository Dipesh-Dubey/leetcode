class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m,n = len(word1),len(word2)
        t = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1,m+1):
            for j in range(1,n+1):
                if word1[i-1] == word2[j-1]:
                    t[i][j] = t[i-1][j-1] + 1
                else:
                    t[i][j] = max(t[i-1][j],t[i][j-1])
        
        count = t[m][n]
        print(count)
        print(len(word1)-count)
        print(len(word2)-count)
        return (len(word1)-count) + (len(word2)-count)