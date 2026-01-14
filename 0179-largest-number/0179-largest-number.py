class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        s_list = []
        for i in range(len(nums)):
            s_list.append(str(nums[i]))
        
        for j in range(len(s_list)):
            for i in range(len(s_list)-j-1):
                sum1 = s_list[i] + s_list[i+1]
                sum2 = s_list[i+1] + s_list[i]

                if int(sum2) > int(sum1):
                    s_list[i] , s_list[i+1] = s_list[i+1] , s_list[i]
        
        return "".join(s_list) if s_list[0] != "0" else "0"