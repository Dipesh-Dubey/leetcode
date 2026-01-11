class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        new = ""
        for c in s:
            if c.isalnum():
                new += c
        
        l = 0
        r = len(new) -1

        while l<=r:
            if new[l] != new[r]:
                return False
            l += 1
            r -= 1

        return True
            