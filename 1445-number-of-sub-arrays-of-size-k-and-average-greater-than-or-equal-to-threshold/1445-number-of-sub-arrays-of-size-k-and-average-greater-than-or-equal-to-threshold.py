class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        le, ri = 0,k
        count = 0
        result =  sum(arr[0 : k])
        if (result)//k >= threshold:
            count += 1
        
        while ri < len(arr):
            result +=  arr[ri] - arr[le]
            if (result)//k >= threshold:
                count += 1
            ri += 1
            le += 1
        return count
            

        