class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1] * len(nums)
        holder = 1
        for i in range(len(nums)):
            ans[i] = holder
            holder *= nums[i]
        holder = 1
        for i in range(len(nums)-1, -1 ,-1 ):
            ans[i] *= holder 
            holder *= nums[i]
        return ans