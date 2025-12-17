class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = []
        for i in range(len(temperatures)-1,-1,-1):
            if len(stack)==0:
                stack.append([temperatures[i],i])
                res.append(0)
            else:                    
                while stack and temperatures[i]>=stack[-1][0]:
                    stack.pop()
                res.append(stack[-1][1]-i) if stack else res.append(0)
                stack.append([temperatures[i],i])
        
        return res[::-1]

