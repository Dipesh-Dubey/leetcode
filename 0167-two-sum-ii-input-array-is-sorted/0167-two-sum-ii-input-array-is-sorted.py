class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        dict = {}
        for i,val in enumerate(numbers):
            diff = target - val
            if diff not in dict:
                dict[val]=i
            else:
                return [dict[diff]+1,i+1]