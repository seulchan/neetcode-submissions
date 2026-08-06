class Solution:
    def countBits(self, n: int) -> List[int]:
        output = [0] * (n + 1)

        for i in range(n+1):
            num = i
            while num > 0:
                output[i] +=1 if num & 1 else 0
                num >>= 1
        
        return output
