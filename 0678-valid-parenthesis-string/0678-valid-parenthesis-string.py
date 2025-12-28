class Solution:
    def checkValidString(self, s: str) -> bool:
        l = 0
        h = 0

        for i in range(len(s)):
            if s[i] == '(':
                l += 1
                h += 1
            elif s[i] == ')':
                l -= 1
                h -= 1
            elif s[i] == '*':
                l -= 1
                h += 1
            
            if l <0:
                l = 0
        
            if h < 0:
                return False
        
        return True if l==0 else False

        
                