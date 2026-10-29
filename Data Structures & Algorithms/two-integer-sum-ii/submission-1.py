class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        right = len(numbers)-1
        left = 0
        while left < right:
            res = numbers[left]+numbers[right]
            if res == target:
                return [left+1, right+1]
            if res > target:
                right-=1
            elif res < target:
                left+=1
        return []
            