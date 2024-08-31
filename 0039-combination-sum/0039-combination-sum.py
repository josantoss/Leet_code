class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def backtrack(start, path, target):
            if target == 0:
                result.append(path)
                return
            if target < 0:
                return
            for i in range(start, len(candidates)):
            # Include the number and move forward
                backtrack(i, path + [candidates[i]], target - candidates[i])

        result = []
        backtrack(0, [], target)
        return result


        