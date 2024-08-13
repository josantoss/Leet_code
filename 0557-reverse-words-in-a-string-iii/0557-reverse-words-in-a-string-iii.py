class Solution:
    def reverseWords(self, s: str) -> str:
        split_str = s.split(" ")
        result = []
        ch = ""
        for ch in split_str:
            ch_1 =  ch[::-1]
            result.append(ch_1)
        return " ".join(result)
