class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        def rec(i,j):
            if i==j: return nums[i]
            left = nums[i] - rec(i+1,j)
            right = nums[j] - rec(i,j-1)

            return max(left,right)
            
        return rec(0,len(nums)-1) >= 0