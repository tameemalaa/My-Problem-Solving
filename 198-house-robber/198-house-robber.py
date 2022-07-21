class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = {}
        def fun(i):
            if i < 0:
                return 0
            if i in dp.keys():
                return dp[i]
            dp[i] = max(nums[i]+fun(i-2),fun(i-1))
            return dp[i]
        return fun(len(nums)-1)