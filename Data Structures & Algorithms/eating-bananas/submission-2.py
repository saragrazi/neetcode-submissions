class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_val = max(piles)
        min_val = 1
        while min_val <= max_val:
            my_hour = h
            k = (max_val+min_val)//2
            for pile in piles:
                my_hour-= (pile + k - 1) // k                    
                if my_hour < 0:
                    min_val = k+1
                    break
            if my_hour >= 0:
                max_val = k-1
        return min_val
