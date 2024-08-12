class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        idx = -1
        for i in range(len(word)):
            if word[i] == ch:
                idx = i
                break
        
        if idx == -1:
            return word
            
        left = word[:idx + 1]
        reverse = left[::-1]
        
        return reverse + word[idx + 1:]



        