class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        '''
        Understand:
            - searchMatrix: [2D array of ints] [int] -> boolean
            - given matrix of ints and a target int, return whether or not that target exists in the matrix
            - each row is sorted in non-decreasing order
            - has to run in O(log(m*n))
        Plan:
            - start in the middle of matrix, so a = matrix[m//2][n//2]
            - if a == target: return true
            - if a < target: have to search to the right of a
                - bring the left pointer to matrix[m//2][n//2 +1]
                - adjust midCol = (m//2 + m) // 2
                - adjust midRow = (n//2+1 + n) // 2
        '''
        # pointers will be coords (row, col)
        left = [0, 0]
        right = [len(matrix)-1, len(matrix[0])-1]

        while ((left[0] < right[0]) or (left[0] == right[0] and left[1] <= right[1])) and (matrix[left[0]][left[1]] <= target and matrix[right[0]][right[1]] >= target):
            mid = [left[0]+right[0]+1 // 2, left[1]+right[1]+1 // 2]
            potentialTarget = matrix[mid[0]][mid[1]]

            if potentialTarget == target:
                return True
            elif potentialTarget < target:
                if mid[1]+1 >= len(matrix[0]):
                    left[0] = mid[0]+1
                    left[1] = 0
                else:
                    left[0] = mid[0]
                    left[1] = mid[1]+1
            elif potentialTarget > target:
                if mid[1]-1 < 0:
                    right[0] = mid[0]-1
                    right[1] = len(matrix[0])-1
                else:
                    right[0] = mid[0]
                    right[1] = mid[1]-1
        return False
            


