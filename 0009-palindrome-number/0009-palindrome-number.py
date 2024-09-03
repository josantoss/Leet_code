class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x = list(str(x))
        if len(x) ==0:
            return False
        else:
            if x == x[::-1]:
                return True
            else:
                return False
        