class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        b = 0
        e = len(nums)
        old_index = -1
        while b<=e :
            index = (b+e)//2
            x = nums[index]
            if x == target: return index
            elif x > target : e = index
            else : b = index
            if old_index == index : 
                if target> nums[index]:
                    return index +1
                else:
                    if index == 0 :
                        return 0
                    return index -1
            old_index = index