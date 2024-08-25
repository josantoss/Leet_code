class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        count = [0] * 26
        l = 0
        maxx = 0
        for r in range(len(s)):
            count[ord(s[r]) - ord('A')] += 1
            while r - l + 1 - max(count) > k:
                count[ord(s[l]) - ord('A')] -= 1
                l += 1
            
            maxx = max(maxx, r - l + 1)
        
        return maxx
        