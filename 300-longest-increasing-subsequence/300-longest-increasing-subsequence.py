class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp= dict()
        def lis(i):
            if i in dp.keys():
                return dp[i]
            if i == 0 :
                dp[i] = 1
                return dp[i]
            dp[i] = 1
            for j in range(i):
                if nums[j] < nums[i]: 
                    #mx=max(mx,lis(j))
                    dp[i] = max(dp[i], lis(j)+1 )
            #dp[i] = mx+dp[i]
            return dp[i]
        for i in range(len(nums)-1,-1,-1):
            lis(i)
        
        print(dp)
        return max(dp.values())
    
    