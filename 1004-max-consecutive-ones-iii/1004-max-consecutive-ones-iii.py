class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = 0
        win = defaultdict(int)
        maxie = 0
        for r in range(len(nums)):
            win[nums[r]] += 1
            while sum(win.values()) - win[1] > k :
                win[nums[l]] -= 1
                if  win[nums[l]] == 0:
                    del win[nums[l]]
                l += 1
            maxie = max(maxie,sum(win.values()))
        
        return maxie