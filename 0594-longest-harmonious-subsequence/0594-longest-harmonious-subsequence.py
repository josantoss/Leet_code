class Solution:
    def findLHS(self, nums: List[int]) -> int:
        nums.sort()
        max_length = 0
        r = 0
        for l in range(len(nums)):
            while r < len(nums) and nums[r] - nums[l] < 2:
                if nums[r] - nums[l] == 1:
                    max_length = max(max_length, r - l + 1)
                r +=1
    
        return max_length
