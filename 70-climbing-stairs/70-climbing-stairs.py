class Solution:
    def climbStairs(self, n: int) -> int:
        z = {1:1,2:2}
        def sol(n):
            if n in z.keys():
                return z[n]
            z[n] = sol(n-1) + sol(n-2)
            return z[n]
        return sol(n)