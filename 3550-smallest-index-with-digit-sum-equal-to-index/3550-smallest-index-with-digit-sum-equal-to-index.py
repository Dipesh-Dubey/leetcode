class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        i = 0
        for num in nums:
            tot = 0
            while num>0:
                tot += num%10
                num = num//10
            
            if tot == i: return i
            else: i+=1
        
        return -1
                 


