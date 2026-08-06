class Solution:
    def countBits(self, n: int) -> List[int]:
        output = [0] * (n + 1)

        for i in range(n+1):
            bin_num = int(bin(i),2)
            count = 0
            while bin_num > 0:
                count +=1 if bin_num & 1 else 0
                bin_num >>= 1
            output[i] = count
        
        return output
