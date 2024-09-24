class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return 0
        max_diff = 0
        nums.sort()
        for i in range(len(nums)-1):
            diff =  nums[i+1] - nums[i]
            max_diff = max(max_diff, diff)
        return max_diff

        