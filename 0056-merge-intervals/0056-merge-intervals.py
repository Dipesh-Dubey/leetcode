class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        stack = []

        for i in range(len(intervals)):
            if not stack:
                stack.append(intervals[i])
            else:
                if intervals[i][0] <= stack[-1][-1]:
                    if intervals[i][-1] > stack[-1][-1]:
                        stack[-1][-1] = intervals[i][-1] 
                else:
                    stack.append(intervals[i])
        
        return stack
