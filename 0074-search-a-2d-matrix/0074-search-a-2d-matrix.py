class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix)-1

        while l<=r:
            mid = (l+r)//2

            if matrix[mid][0] <= target <= matrix[mid][len(matrix[mid])-1] :
                break
            
            elif matrix[mid][0] < target:
                l = mid + 1
            else:
                r = mid - 1
        
        l = 0
        r = len(matrix[mid])-1

        while l<=r:
            mid_1 = (l+r)//2

            if matrix[mid][mid_1] == target:
                return True
            elif matrix[mid][mid_1] > target:
                r = mid_1 - 1
            else:
                l = mid_1 + 1
        
        return False