class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def hours_needed(speed):
            return sum(math.ceil(p / speed) for p in piles)
        lo, hi = 1, max(piles)            # answer range: 1 .. biggest pile
        while lo < hi:
            mid = (lo + hi) // 2
            if hours_needed(mid) <= h:    
                hi = mid
            else:                          # too slow -> must go faster
                lo = mid + 1
        return lo                          # smallest feasible speed

