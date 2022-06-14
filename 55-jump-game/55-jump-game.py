class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) ==1 :
            return True
        zeros= 0
        for i in range(len(nums)-1,-1,-1):
            if nums[i] == 0:
                zeros+=1
            else : 
                if nums[i]> zeros or (nums[i] == zeros and i+nums[i] == len(nums)-1) :
                    zeros =0
                else :
                    zeros +=1
        return zeros == 0