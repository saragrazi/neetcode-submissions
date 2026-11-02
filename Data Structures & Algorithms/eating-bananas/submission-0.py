class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_val = max(piles)
        min_val = 1
        res = float('inf')
        while min_val <= (max_val+min_val)//2:
            my_hour = h
            k = (max_val+min_val)//2
            for i, pile in enumerate(piles):
                my_hour-= math.ceil(pile / k)
                if i == len(piles)-1 and my_hour>=0:
                    res = min(res, k)
                    max_val = k-1
                if my_hour < 0:
                    min_val = k+1
                    break
        return res
