class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        while True:
            st,p = str(n), 1

            for s in st:
                p *= int(s)
            
            # print(p)
            if p%t==0: return int(st)
            n += 1
