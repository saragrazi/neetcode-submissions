class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        
        while start <= end:
            med = (start + end) // 2
            
            if target == nums[med]:
                return med
                
            if nums[start] <= nums[med]:
                if nums[start] <= target < nums[med]:
                    end = med - 1
                else:
                    start = med + 1
            else:
                if nums[med] < target <= nums[end]:
                    start = med + 1
                else:
                    end = med - 1
        return -1