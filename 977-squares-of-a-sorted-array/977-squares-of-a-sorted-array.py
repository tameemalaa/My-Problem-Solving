class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        a = []
        while nums :
            if abs(nums[0]) >= abs(nums[-1]):
                a.insert(0,nums[0]**2)
                nums.pop(0)
            else :
                a.insert (0,nums[-1]**2)
                nums.pop(-1)
        return a