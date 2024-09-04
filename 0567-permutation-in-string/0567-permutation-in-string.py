class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        ## first count the frequency of each string
        s1_Count, s2_Count = [0] * 26, [0] * 26
        l1, l2 = len(s1), len(s2)
        
        if l1 > l2:
            return False
        for i in range(l1):
            s1_Count[ord(s1[i]) - ord('a')] += 1
            s2_Count[ord(s2[i]) - ord('a')] += 1
        for i in range(l1, l2):
            if s1_Count == s2_Count:
                return True
            s2_Count[ord(s2[i]) - ord('a')] += 1
            s2_Count[ord(s2[i - l1]) - ord('a')] -= 1
        return s1_Count == s2_Count