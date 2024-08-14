class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        nums.sort()
        left , right = 0, len(nums) - 1
        array =[]
        while left < right:
            average = ((nums[left]+ nums[right])/2 )
            array += [average]
            left += 1
            right -= 1
             
        return min(array)        