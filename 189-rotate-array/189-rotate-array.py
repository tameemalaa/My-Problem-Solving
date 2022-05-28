class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        x = nums[:]
        print(x)
        print(nums)
        for i in range(len(nums)):
            nums[(i+k)%len(nums)]=x[i]
        