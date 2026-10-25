class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        my_nums = set()
        my_max = 0
        for num in nums:
            my_nums.add(num)
        for num in nums:
            if num-1 not in my_nums:
                max_now = 1
                while num+1 in my_nums:
                    max_now+=1
                    num += 1
                my_max = max(my_max, max_now)
        return my_max

        
        