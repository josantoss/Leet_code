class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        size = len(nums)
        pos, neg = 0, 1
        output = [0]*size
        for num in nums:
            if num < 0:
                output[neg] = num
                neg += 2
            else:
                output[pos] = num
                pos += 2
        return output   