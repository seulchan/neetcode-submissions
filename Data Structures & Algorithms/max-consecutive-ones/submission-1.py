class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_ones = 0
        ones = 0
        for num in nums: 
            if num == 1:
                ones += 1
            else:  
                ones = 0
            
            if ones > max_ones:
                max_ones = ones
                
        return max_ones