class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        m, n = len(num1), len(num2)
        res = [0] * (m + n)

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                mul = int(num1[i]) * int(num2[j])

                p1 = i + j
                p2 = i + j + 1

                total = mul + res[p2]

                res[p2] = total % 10
                res[p1] += total // 10

        ans = []

        for num in res:
            if not (len(ans) == 0 and num == 0):
                ans.append(str(num))

        return "".join(ans)