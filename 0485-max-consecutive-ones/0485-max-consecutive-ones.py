class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        maxi = []
        for i,v in enumerate(nums):
            if v == 1:
                count +=1
            
            if v == 0:
                maxi.append(count)
                count = 0
        
        maxi.append(count)
        return max(maxi)