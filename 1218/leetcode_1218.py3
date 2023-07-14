class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        maxCount = 1
        arthimetic_sequence={}
        for i in arr:
            if i-difference in arthimetic_sequence:
                arthimetic_sequence[i]=1+arthimetic_sequence[i-difference]
            else:
                arthimetic_sequence[i]=1
            maxCount=max(maxCount,arthimetic_sequence[i])
        return maxCount




        
