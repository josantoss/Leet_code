class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        l = 0
        total = sum(arr[:k - 1])
        count = 0
        for r in range(k - 1, len(arr)):
            total += arr[r]
            if total // k >= threshold:
                count += 1
            total -= arr[l]
            l += 1
        
        return count
            
            

            

        