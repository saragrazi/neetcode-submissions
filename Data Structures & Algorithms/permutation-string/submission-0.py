class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        dict_s1 = {}
        dict_s2 = {}
        for char in s1:
            dict_s1[char] = dict_s1.get(char, 0) + 1
        left = 0 
        right = len(s1) - 1
        for i in range(right):
            dict_s2[s2[i]] = dict_s2.get(s2[i], 0) + 1
        while right < len(s2):
            dict_s2[s2[right]] = dict_s2.get(s2[right], 0) + 1
            if dict_s1 == dict_s2:
                return True
            dict_s2[s2[left]] -= 1
            if dict_s2[s2[left]] == 0:
                del dict_s2[s2[left]]
            left += 1
            right +=1
        return False