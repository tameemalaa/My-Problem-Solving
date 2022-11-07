class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        length = len(nums1) + len(nums2)
        half = length //2
        if len(nums2) < len(nums1):
            nums1,nums2 = nums2,nums1 
        s = 0
        e = len(nums1)-1

        while True :
            m1 = (s+e) //2
            m2 = half - m1 -2
            left1 = nums1[m1] if m1 >=0 and nums1 else -float(inf)
            right1 = nums1[m1+1] if m1+1 < len(nums1) else float(inf)
            left2 = nums2[m2]  if m2 >=0 and nums2 else -float(inf)
            right2= nums2[m2+1]  if m2+1 < len(nums2) else float(inf)
            if left1 <= right2 and left2 <= right1 :
                if length % 2 :
                    return min(right1,right2)
                else:
                    return (max(left1,left2) + min(right1,right2)) /2
            if left1 > right2 : e = m1-1
            else : s = m1+1