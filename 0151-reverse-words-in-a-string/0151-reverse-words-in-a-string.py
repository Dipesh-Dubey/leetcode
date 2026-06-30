class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split(" ")
        ans = ""
        for i in range(len(s)-1,-1,-1):
            if s[i] != "":
                ans = ans + s[i] + " "

        return ans[:len(ans)-1]
        