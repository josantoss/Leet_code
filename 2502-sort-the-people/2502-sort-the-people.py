class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        for i in range(len(heights)):
            max_value = i
            for j in range(i+1,len(heights)):
                if heights[max_value] < heights[j]:
                    max_value = j
            heights[i],heights[max_value] = heights[max_value] ,heights[i]
            names[i], names[max_value] = names[max_value], names[i]
        return names    
        