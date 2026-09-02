class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top = 0
        bottom = len(matrix)-1

        while top <= bottom:
            mid = (top + bottom) // 2

            lowEnd = matrix[mid][0]
            highEnd = matrix[mid][-1]

            if lowEnd <= target and highEnd >= target:
                left = 0
                right = len(matrix[0])-1
                
                while left <= right:
                    midCol = (left + right) // 2
                    potentialTarget = matrix[mid][midCol]
                    
                    if potentialTarget == target:
                        return True
                    elif potentialTarget < target:
                        left = midCol+1
                    elif potentialTarget > target:
                        right = midCol-1
                return False
            elif lowEnd > target:
                bottom = mid-1
            elif highEnd < target:
                top = mid+1
            
        return False
                
                    



            