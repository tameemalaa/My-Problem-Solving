class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        return [i for i in  nums  if not(i%2)] + [i for i in  nums  if i%2] 