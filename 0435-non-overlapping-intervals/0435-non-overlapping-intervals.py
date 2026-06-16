class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        count = 0
        intervals.sort(key=lambda x: x[0])

        res = []

        for start, end in intervals:
            if not res or start >= res[-1][1]:
                res.append([start, end])
            else:
                count+=1
                if end < res[-1][1]:
                    res.pop()
                    res.append([start, end])

        return count