class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            if target >= row[0] and target <= row[-1]:
                return self.binarySearch(row, target)
        return False    
        
    
    def binarySearch(self, row: List[int], target: int) -> bool:
        i = 0
        j = len(row)-1
        while i <= j:
            mid = (i+j)//2
            if row[mid] == target:
                return True
            elif row[mid] < target:
                i = mid + 1
            else:
                j = mid-1
        return False