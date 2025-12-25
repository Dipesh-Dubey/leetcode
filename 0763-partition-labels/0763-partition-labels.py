class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        h = {}
        for i,v in enumerate(s):
           h[v] = i
        
        size,end = 0,0
        res = []
        for i,v in enumerate(s):
            size+=1
            end = max(end,h[v])

            if i == end:
                res.append(size)
                size,end = 0,0
                continue
        
        return res

