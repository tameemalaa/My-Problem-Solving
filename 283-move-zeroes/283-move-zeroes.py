class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        k = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[k] = nums[i] 
                k+=1 
        l = len(nums) -k
        while l != 0:
            nums[-l]=0
            l-=1
        
            
                
                
                