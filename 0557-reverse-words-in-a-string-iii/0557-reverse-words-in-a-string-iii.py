class Solution:
    def reverseWords(self, s: str) -> str:
        s_List = list(s)
        left = 0
        for right in range(len(s_List)):
            if s_List[right] == " " or right == len(s_List)-1:
                temp_l, temp_r = left, right-1
                if right == len(s_List) -1 :
                    temp_r = right
                while temp_l< temp_r:
                    s_List[temp_l], s_List[temp_r] = s_List[temp_r], s_List[temp_l]
                    temp_l += 1
                    temp_r -= 1
                left = right + 1
        return "".join(s_List)
                    
