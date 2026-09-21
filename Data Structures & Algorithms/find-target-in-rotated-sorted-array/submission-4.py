class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        # finding the min
        while l < r:
            mid = (l+r) // 2
            if nums[mid] > nums[r]:
                l = mid+1
            else:
                r = mid
        
        # from the min, we know where the subarrays are split
        pivot = l

        if nums[pivot] == target:
            return pivot

        # perform binary search on both sides
        subArrLeftOfPiv = 0
        rightOfSubArr = pivot-1
        
        while subArrLeftOfPiv <= rightOfSubArr:
            mid = (subArrLeftOfPiv + rightOfSubArr) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                rightOfSubArr = mid-1
            else:
                subArrLeftOfPiv = mid+1
        
        subArrRightOfPiv = pivot
        rightOfRightSubArr = len(nums)-1

        while subArrRightOfPiv <= rightOfRightSubArr:
            mid = (subArrRightOfPiv + rightOfRightSubArr) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                rightOfRightSubArr = mid-1
            else:
                subArrRightOfPiv = mid+1

                    
        return -1
                    



