class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counter1,counter2 = 0,0
        candid1 , candid2 = None,None

        for num in nums:
            if num == candid1:
                counter1 += 1
            elif num == candid2:
                counter2 += 1
            elif counter1 == 0:
                counter1 = 1
                candid1 = num
            elif counter2 == 0:
                counter2 = 1
                candid2 = num
            else:
                counter1 -= 1
                counter2 -= 1
        
        res = []
        if nums.count(candid1) > len(nums)// 3:
            res.append(candid1)
        if nums.count(candid2) > len(nums)// 3:
            res.append(candid2)
        return res