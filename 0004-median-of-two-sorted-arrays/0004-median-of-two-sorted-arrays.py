class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        num = nums1 + nums2
        num.sort()
        total_len = len(num)
        half = (total_len)//2
        if (total_len % 2 == 0):
            return (num[half - 1]+num[half])/2.0
        else:
            return num[half] 
        