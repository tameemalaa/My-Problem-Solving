class Solution:
    def fib(self, n: int) -> int:
        z = {0:0,1:1,2:1}
        def sol(n):
            if n in z.keys():
                return z[n]
            z[n] = sol(n-1) + sol(n-2)
            return z[n]
        return sol(n)