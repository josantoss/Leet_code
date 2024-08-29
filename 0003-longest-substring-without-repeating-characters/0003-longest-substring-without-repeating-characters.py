class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = 0
        r = 0
        

        longest = 0 
        hashset = set()
        while r < len(s):
            if s[r] not in hashset:
                hashset.add(s[r])
                r += 1
                longest = max(longest, r - l)
            else:
                hashset.remove(s[l])
                l += 1            
        return longest
        