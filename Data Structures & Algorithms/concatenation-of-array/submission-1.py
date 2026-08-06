class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        N = len(nums)
        ans = [0] * (2 * N)
        
        for idx, num in enumerate(nums):
            ans[idx] = ans[idx + N] = num
        
        return ans
