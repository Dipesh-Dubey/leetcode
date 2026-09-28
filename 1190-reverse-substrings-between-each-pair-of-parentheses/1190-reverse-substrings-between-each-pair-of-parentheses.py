class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []

        for c in s:
            if c != ")" or not stack:
                stack.append(c)
            
            if c==")":
                res = ""
                while stack[-1] != "(" and stack:
                    res += stack.pop()
                stack.pop()
                
                for i in res:
                    stack.append(i)
            
        return "".join(stack)