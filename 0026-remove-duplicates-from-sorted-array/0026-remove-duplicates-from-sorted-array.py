class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hashSet = set()
        i = 0
        while i < len(nums):
            if nums[i] not in hashSet:
                hashSet.add(nums[i])
                i += 1
            else:
                del nums[i]
        
        # Optionally extend with dashes
        # nums.extend(['-'] * (len(nums) - len(hashSet)))
        
        return len(nums)


        