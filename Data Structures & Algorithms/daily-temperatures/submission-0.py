class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        stack = []

        for i, cur_temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < cur_temp:
                idx = stack.pop()
                ans[idx] = i-idx
            stack.append(i)
        
        return ans