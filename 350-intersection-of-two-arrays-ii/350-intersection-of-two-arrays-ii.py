from collections import Counter
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        c1 = Counter(nums1)
        c2 = Counter(nums2)
        c =[]
        for i in c1.keys() : 
            if i in c2.keys():
                c.extend([i]*(min(c1[i],c2[i])))
        return c