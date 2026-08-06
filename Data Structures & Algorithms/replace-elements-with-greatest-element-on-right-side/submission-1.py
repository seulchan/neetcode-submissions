class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        N = len(arr)
        ans = [0] * N
        rightMax = -1
        for i in range(N - 1, -1, -1):
            ans[i] = rightMax
            rightMax = max(arr[i], rightMax)
        return ans