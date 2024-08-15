class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest_l = 0
        longest_r = 0
        for i in range(len(s)):
            # for even length
           
            left,right = i,i+1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if (right -left > longest_r - longest_l):
                    longest_l = left
                    longest_r = right
                left -= 1
                right += 1
            left, right = i,i
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if (right -left > longest_r - longest_l):
                    longest_l = left
                    longest_r = right
                left -= 1
                right += 1               
        return s[longest_l:longest_r+1]
                
        
        
        