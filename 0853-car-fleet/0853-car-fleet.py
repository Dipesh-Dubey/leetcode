class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [[p,s] for p,s in zip(position,speed)]
        pair = sorted(pair)
        stack = []
        time = [(target - p)/s for p,s in pair]

        for i in range(len(time)-1,-1,-1):
            if not stack:
                stack.append(time[i])
            else:
                if time[i]<=stack[-1]:
                    continue
                else:
                    stack.append(time[i])
            
        return len(stack)


            
            
