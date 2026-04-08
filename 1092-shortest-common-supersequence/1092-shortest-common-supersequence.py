class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        m,n = len(str1),len(str2)
        t = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1,m+1):
            for j in range(1,n+1):
                if str1[i-1] == str2[j-1]:
                    t[i][j] = t[i-1][j-1] + 1
                else:
                    t[i][j] = max(t[i-1][j],t[i][j-1])
        
        i,j = m,n
        res = []  
        while i>0 or j>0:
            if i==0:
                res.append(str2[j - 1])
                j -= 1
            elif j==0:
                res.append(str1[i - 1])
                i -= 1
                
            elif str1[i-1] == str2[j-1]:
                res.append(str1[i-1])
                i-=1
                j-=1
            else:
                if t[i][j-1] < t[i-1][j]:
                    res.append(str1[i-1])
                    i-=1
                else:
                    res.append(str2[j-1])
                    j-=1

        return "".join(res[::-1])


        