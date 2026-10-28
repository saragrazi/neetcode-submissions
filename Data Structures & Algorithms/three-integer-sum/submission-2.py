class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res = []
        n = len(nums)
        
        for i in range(n - 2):
            # 1. דילוג על כפילויות מול האיטרציה הקודמת
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            # 2. left מתחיל תמיד מימין ל-i
            left = i + 1
            right = n - 1
            
            while left < right:
                myres = nums[i] + nums[left] + nums[right]
                
                # 3. כיווני הזזה נכונים
                if myres < 0:
                    left += 1      # הסכום קטן מדי -> מגדילים
                elif myres > 0:
                    right -= 1     # הסכום גדול מדי -> מקטינים
                else:
                    res.append([nums[i], nums[left], nums[right]])
                    
                    # דילוג על כפילויות של left ו-right
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    
                    left += 1
                    right -= 1
                    
        return res