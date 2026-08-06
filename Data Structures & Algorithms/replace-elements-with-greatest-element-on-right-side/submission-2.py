class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        rightMax = -1
        N = len(arr)
        
        for i in range(N-1, -1, -1):
            cur_val = arr[i]
            arr[i] = rightMax
            rightMax = max(rightMax, cur_val)
        
        return arr