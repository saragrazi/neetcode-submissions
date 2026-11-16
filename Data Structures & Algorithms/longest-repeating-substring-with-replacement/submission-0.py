class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count ={}
        left = 0
        res = 0
        max_amount = 0
        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0)+1
            max_amount = max(max_amount, count[s[r]])
            while r-left+1 - max_amount > k:
                count[s[left]]-=1
                left+=1
            res = max(res, r-left+1)
        return res