class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        N = len(nums)
        ans = [0] * (N * 2)
        

        for i, num in enumerate(nums):
            ans[i] = ans[i+N] = num
        
        return ans
