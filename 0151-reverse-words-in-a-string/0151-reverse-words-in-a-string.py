class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        word = s.split()
        reverse_Words = word[::-1]
        return " ".join(reverse_Words)