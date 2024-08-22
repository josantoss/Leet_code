class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        j = 1
        right = 1
        while right<len(nums) and j < len(nums):
            if j < 2 or nums[right] > nums[j - 2]:
                nums[j] = nums[right]
                j += 1
            right += 1 
        return j
