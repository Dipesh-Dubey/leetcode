class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = max(weights)
        r = sum(weights)

        while l<=r:
            
            mid_cap = (l+r)//2

            days_needed = 1
            curr_tot = 0
            for w in weights:
                if w+curr_tot> mid_cap :
                    days_needed+=1
                    curr_tot = w
                else:
                    curr_tot += w

            if days_needed<=days:
                r = mid_cap-1            
            else:
                l = mid_cap+1
        
        return l