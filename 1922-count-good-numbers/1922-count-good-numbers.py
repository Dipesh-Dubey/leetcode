class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod = 10**9 + 7

        def pow(x,n):
            res = 1
            while n>0:
                if n%2 != 0:
                    res = (res*x)%mod
                n = n//2
                x = (x*x)%mod
            
            return res

        if n%2==0:
            return ((pow(5,n//2)%mod)*(pow(4,n//2)%mod))%mod
        else:
            return ((pow(5,(n + 1)//2)%mod)*(pow(4,n//2)%mod))%mod

        


