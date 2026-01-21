class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        if n==1: #edge
            return "0"

        s = "1"
        l,r = 0 , (2**n - 1)-1

        while l<=r:
            mid = (l+r)//2
            if k-1 == mid:
                return s
            if k-1 < mid:
                r = mid-1
                s = "1"
                if l==r:
                    return "0"
            else:
                l = mid+1
                s = "0"
                if l==r:
                    return "1"
        
        
