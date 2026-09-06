class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        
        total = sum(nums)

        if total % 2 != 0:
            return False

        target = total // 2

        dp = [[-1] * (target + 1) for _ in range(n)]

        def dfs(i, target):
            # We found a subset with required sum
            if target == 0:
                return True

            # No elements left
            if i == n:
                return False

            # Already calculated
            if dp[i][target] != -1:
                return dp[i][target]

            # Take or skip nums[i]
            if nums[i] <= target:
                dp[i][target] = (
                    dfs(i + 1, target - nums[i])
                    or dfs(i + 1, target)
                )
            else:
                dp[i][target] = dfs(i + 1, target)

            return dp[i][target]

        return dfs(0, target)