class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        #edge case
        if len(bloomDay) < m*k:
            return -1
        
        l,r = min(bloomDay),max(bloomDay)

        while l<=r:
            mid = (l+r)//2
            bouquets,counter = 0,0

            for i in range(len(bloomDay)):
                if bloomDay[i] > mid:
                    counter = 0
                if bloomDay[i] <= mid and counter!=k-1:
                    counter +=1
                elif bloomDay[i] <= mid and counter==k-1:
                    counter = 0
                    bouquets +=1
                #print(mid,counter,bouquets)
            
            #print(mid,bouquets)
                
            if bouquets >= m:
                r = mid - 1

            else:
                l = mid + 1
            
            #print(l,r)
            
        return l