class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        num = ""
        res = ""
        for ch in s:
            if ch in "0123456789":
                num += ch
            elif ch == "[":
                stack.append(int(num))
                stack.append(ch)
                num = ""
            elif ch != "]":
                stack.append(ch)
            else:
                popped = ""
                state = ""
                while stack[-1]!="[":
                    popped = stack.pop() + popped
                stack.pop()
                val = stack.pop()
                stack.append(popped*val)
        for i in range(len(stack)):
            res += stack[i]
        return res

            
        

