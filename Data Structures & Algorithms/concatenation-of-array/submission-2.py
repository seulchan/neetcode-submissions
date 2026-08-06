class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        N = len(nums)
        ans = [0] * (2 * N)
        
        for i, num in enumerate(nums):
            ans[i] = ans[i + N] = nums[i]
        
        return ans
