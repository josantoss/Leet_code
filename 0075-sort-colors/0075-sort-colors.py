class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = {}
        for element in range(len(nums)):
            count[nums[element]] = count.get(nums[element], 0) + 1
        index = 0
        for color in range(3):
            value = count.get(color,0)
            nums[index: index + value] = [color]*value
            index += value
