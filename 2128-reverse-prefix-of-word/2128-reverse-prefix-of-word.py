class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        word = list(word)
        right = word.index(ch) if ch in word else -1

        if right != -1:
            left = 0
            while left < right:
                word[left], word[right] = word[right], word[left]
                left += 1
                right -= 1
        return "".join(word)


        