from math import ceil 
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        while nums :
            index = int(ceil(len(nums)) - 1)
            x = nums[index]
            print(x)
            if x == target: return index
            elif x > target : nums = nums[:index]
            else : nums = nums[index+1:]
        
        return -1