class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        res = {}
        
        for num in nums:
            res[num] = 1 + res.get(num, 0)
            if res[num] > 1:
                return True

        return False

