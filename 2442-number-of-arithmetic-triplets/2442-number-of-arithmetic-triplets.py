class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        sett = set(nums)
        count = 0
        for n in nums:
            if n + diff in sett and n + 2 * diff in sett:
                count += 1
        
        return count
        

        