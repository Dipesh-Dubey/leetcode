class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)

        while l<=r:
            mid = (l+r)//2

            h_needed = 0
            for b in piles:
                if mid >= b:
                    h_needed += 1
                else:
                    h_needed += (b + mid - 1)//mid

            if h_needed <= h:
                r = mid - 1
            else:
                l = mid + 1
        
        return l