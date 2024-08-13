class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for s in words:
            if self.checkPalindrom(s):
                return s
        return ""
    def checkPalindrom(self, s : str) -> bool:
        left, right = 0, len(s) -1
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True


                

        