class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def neededHour(eat):
            return sum([math.ceil(pile / eat) for pile in piles])

        low = 1
        high = max(piles)
        k = high

        while low <= high:
            mid = (low + high) // 2

            if neededHour(mid) <= h:
                high = mid - 1
                k = mid
            else: 
                low = mid + 1
            
        return k

