class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ones, max_ones = 0, 0

        for num in nums:
            if num == 0:
                max_ones = max(ones, max_ones)
                ones = 0
            else:
                ones += 1
        
        return max(ones, max_ones)