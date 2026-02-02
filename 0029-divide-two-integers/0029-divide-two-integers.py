class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == -2**31 and divisor == -1:
            return (2**31) - 1

        s = 1
        if (dividend>0 and divisor<0) or (dividend<0 and divisor>0):
            s = -1

        dividend = abs(dividend)
        divisor = abs(divisor)
        res = 0
        while dividend>=divisor:
            cnt = 0
            while dividend >= divisor*(2**(cnt+1)):
                cnt += 1
            res += 2**cnt
            dividend -= divisor * (2**cnt)

        return min(max(s*res , -2**31), 2**31 - 1)