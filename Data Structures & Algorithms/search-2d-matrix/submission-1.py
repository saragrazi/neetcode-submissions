class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        right = len(matrix)-1
        up = 0
        while right >= 0 and up < len(matrix[0]):
            if matrix[right][up] == target:
                return True
            if matrix[right][up] > target:
                right-=1
            elif matrix[right][up] < target:
                up+=1
        return False


            