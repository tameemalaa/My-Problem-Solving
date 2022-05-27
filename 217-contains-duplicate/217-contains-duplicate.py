from collections import Counter 
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        c = Counter(nums)
        if len(nums) == len(c): return False 
        else : return True
        
        