class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key = lambda x:len(x))
        print(words)
        n = len(words)
        dp = [[-1] * (n + 1) for _ in range(n)]

        def isPred(shorter, longer):
            if len(longer) != len(shorter) + 1:
                return False

            p1 = p2 = 0

            while p1 < len(shorter) and p2 < len(longer):
                if shorter[p1] == longer[p2]:
                    p1 += 1
                    p2 += 1
                else:
                    p2 += 1

            return p1 == len(shorter)

        def dfs(i, prev):
            if i == n:
                return 0

            if dp[i][prev + 1] != -1:
                return dp[i][prev + 1]

            if prev == -1 or isPred(words[prev], words[i]):
                dp[i][prev + 1] = max(1 + dfs(i+1, i), dfs(i+1, prev))

            else:
                dp[i][prev + 1] = dfs(i + 1, prev)

            return dp[i][prev + 1]

        return dfs(0, -1)
    