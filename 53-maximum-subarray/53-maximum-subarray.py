class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        summ = 0
        g_max = float('-inf')
        
        for num in nums:
            summ+= num
            g_max = max(g_max,summ)
            if summ <0: summ=0
        return g_max
        