
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        global_max = -10**5
        local_max = 0
        for i in range(len(nums)) : 
            local_max += nums[i]
            global_max= max((local_max , global_max))
            if (local_max <0) : local_max = 0
        return global_max
                