class Solution:
    def myPow(self, x: float, n: int) -> float:
        num = n
        if num < 0:
            return 1.0 / self.power(x, -num)

        return self.power(x, num)
        
    def power(self,x,n):
        if n==0:
            return 1
        if n%2==0:
            return self.power(x * x, n // 2)       
        else:
            return x * self.power(x, n - 1)