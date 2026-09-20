class Solution:
    def reverseDegree(self, s: str) -> int:
        n = len(s)
        tot = 0
        for i in range(n):
            tot += ((-ord(s[i]) + ord('z') + 1)*(i+1))

        return tot