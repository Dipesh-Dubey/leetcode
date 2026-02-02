class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        count = 0
        while start or goal:
            n1 = start % 2
            n2 = goal % 2
            if n1 != n2:
                count +=1 
            
            start = start//2
            goal = goal//2

        return count