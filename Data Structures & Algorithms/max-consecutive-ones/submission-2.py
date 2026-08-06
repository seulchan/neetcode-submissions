class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_val = val = 0

        for num in nums:
            if num == 1:
                val += 1
            else:
                max_val = max(max_val, val)
                val = 0
        
        return max(max_val, val)