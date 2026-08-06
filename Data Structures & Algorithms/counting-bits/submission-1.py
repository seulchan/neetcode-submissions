class Solution:
    def countBits(self, n: int) -> List[int]:
        output = [0] * (n + 1)

        for i in range(n+1):
            index = i
            count = 0
            while i > 0:
                count +=1 if i & 1 else 0
                i >>= 1
            output[index] = count
        
        return output
