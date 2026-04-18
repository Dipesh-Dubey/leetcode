class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        n = len(nums)
        map  = defaultdict(int)

        def rev(num):
            ans = 0 
            while num>0:
                dig = num%10
                num = num//10
                ans = (ans*10) + dig
            return ans

        mini = n+1
        for i in range(n):
            if nums[i] not in map:
                map[rev(nums[i])] = i

            else:
                mini = min(mini,abs(i-map[nums[i]]))
                map[rev(nums[i])] = i


        if mini == n+1: return -1
        else: return mini
                