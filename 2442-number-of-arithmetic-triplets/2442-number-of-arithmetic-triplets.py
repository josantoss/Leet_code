class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        count = 0
        j, k = 1, 2
        for i in range(len(nums) - 2):
            while j < len(nums) - 1 and nums[j] - nums[i] < diff:
                j += 1
            while k < len(nums) and nums[k] - nums[j] < diff:
                k += 1
            
            if k < len(nums) and nums[j] - nums[i] == nums[k] - nums[j] == diff:
                count += 1
        return count


        