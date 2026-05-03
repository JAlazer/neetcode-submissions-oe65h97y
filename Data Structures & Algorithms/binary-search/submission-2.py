class Solution:
    def search(self, nums: List[int], target: int) -> int:
        '''
        Understand:
            - search: [array of ints] [int] -> int
            - given an array of distinct ints sorted in ascending order, and a target, return idx of target or -1 if it DNE
            - ex: [-1, 0, 2, 4, 6, 8], 3
                - mid = 6 / 2 = 3
                - nums[mid] = 4 != 3  
        Plan:
            Recursive:
                Base cases:
                    - if len(nums) == 0:
                        return -1

                    mid = len(nums) // 2
                    
                    - if nums[mid] == target:
                        return mid
                Recurse:
                    leftTargetIdx = search(nums[0:mid], target)
                    rightTargetIdx = search(nums[mid+1, len(nums)], target)

                    if leftTargetIdx == -1 and rightTargetIdx == -1:
                        return -1
                    elif leftTargetIdx == -1:
                        return rightTargetIdx
                    else:
                        return leftTargetIdx
                
        '''

        if len(nums) == 0:
            return -1
        left = 0
        right = len(nums) - 1
        

        while left <= right:
            mid = (left + right + 1) // 2
            if nums[mid] == target:
                return mid

            if target > nums[mid]:
                left = mid + 1
            if target < nums[mid]:
                right = mid - 1
        
        return -1
