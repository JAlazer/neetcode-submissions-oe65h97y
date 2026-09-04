class Solution:
    """
    Understand:
        - minEatingSpeed: [list of ints] [int] -> [int]
        - given a list of piles where piles[i] is the number of bananas in the ith pile, h which represents the number of hours to eat the bananas, return the minimum k (rate of bananas per hour) to finish eating all bananas within h hours
        - notes:
            - each hour you choose to eat k bananas from a pile
            - cannot eat from another pile in the same hour
    """
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        result = r

        while l <= r:
            potentialRate = (l + r) // 2

            hoursSpent = 0
            for bananas in piles:
                hoursOnPile = math.ceil(bananas / potentialRate)

                hoursSpent += hoursOnPile
            
            if hoursSpent <= h:
                result = potentialRate
                r = potentialRate - 1
            elif hoursSpent > h:
                l = potentialRate + 1
                

        return result
            
        