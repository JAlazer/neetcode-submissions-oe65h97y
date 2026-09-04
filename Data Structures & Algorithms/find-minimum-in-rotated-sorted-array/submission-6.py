class Solution:
    '''
    Understand:
        - given array (of unique elements) that has been rotated btwn 1 ... n times, return minimum element of the array in O(log n)
        - ex: [3, 4, 5, 6, 1, 2]
            - l = 0
            - r = 5
            - mid = 5 // 2 = 2
            - compare:
                - 3 < 5 -> good
                - 2 < 5 -> bad -> shift search right (l = mid+1)
            - now:
                - l = 3
                - r = 5
                - mid = 8 // 2 = 4
                - compare:
                    - 6 > 1 -> bad, but want mid cuz it's less, so (r = mid)
            - now:
                - l = 3
                - r = 4
                - mid = 7 // 2 = 3
                - compare:
                    - 6 == 6
                    - 1 < 6 -> bad -> shift search (l=mid+1)
            - now:
                - l = 5
                - r = 4
                - return res

    '''
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        res = l
        while l < r:
            mid = (l+r) // 2

            if nums[mid] > nums[r]:
                l = mid+1
            else:
                r = mid
        return nums[l]

        