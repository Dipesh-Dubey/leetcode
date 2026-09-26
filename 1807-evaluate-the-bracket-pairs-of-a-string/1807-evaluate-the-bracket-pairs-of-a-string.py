class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        n = len(knowledge)
        d = {}

        for i in range(n):
            d[knowledge[i][0]] = knowledge[i][1]    
        # print(d)
        
        stack = []
        for c in s:
            if not stack or c != ")":
                stack.append(c)
            
            else:
                key = ""
                while stack[-1] != "(" and stack:
                    key += stack.pop()
                stack.pop()
                key = key[::-1]
                print(key)

                if key in d.keys():
                    stack.append(d[key])
                else:
                    stack.append("?")

        # print(stack)
        return "".join(stack)

    