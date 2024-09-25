class Solution(object):
    def dividePlayers(self, skill):
        """
        :type skill: List[int]
        :rtype: int
        """
        skill.sort()
        leng = len(skill)
        if leng%2 ==1 or leng == 0:
            return -1
        chem = 0
        target = skill[0] + skill[-1]
        l, r = 0, leng - 1
        while l < r:
            if skill[l] + skill[r] != target:
                return -1
            chem += skill[l]*skill[r]
            l += 1 
            r -= 1
        return chem
        