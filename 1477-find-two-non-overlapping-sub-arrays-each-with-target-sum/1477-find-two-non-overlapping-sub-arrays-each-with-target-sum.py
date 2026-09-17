class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        n = len(arr)
        left = [float("inf")] * n

        prefix = 0
        mp = {0: -1}
        best = float("inf")

        for i in range(n):
            prefix += arr[i]

            if prefix - target in mp:
                j = mp[prefix - target]
                length = i - j
                best = min(best, length)

            left[i] = best
            mp[prefix] = i

        prefix = 0
        mp = {0: n}
        best = float("inf")
        ans = float("inf")

        for i in range(n - 1, -1, -1):
            prefix += arr[i]

            if prefix - target in mp:
                j = mp[prefix - target]
                length = j - i
                best = min(best, length)

            if i > 0 and left[i - 1] != float("inf") and best != float("inf"):
                ans = min(ans, left[i - 1] + best)

            mp[prefix] = i

        return -1 if ans == float("inf") else ans