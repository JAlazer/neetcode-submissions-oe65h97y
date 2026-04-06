# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def isCarry(sumVal):
    if sumVal > 9:
        return True
    else:
        return False

def getPointerSum(pointer1, pointer2, givenCarry):
    if givenCarry:
        if pointer1 and pointer2:
            return pointer1.val + pointer2.val + 1
        if pointer1:
            return pointer1.val + 1
        if pointer2:
            return pointer2.val + 1
    else:
        if pointer1 and pointer2:
            return pointer1.val + pointer2.val
        if pointer1:
            return pointer1.val
        if pointer2:
            return pointer2.val
    return 0


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        '''
        Understand:
            - addTwoNumbers: [LinkedList] [ LinkedList] -> [LinkedList]
            - goal: given two linked lists, return the sum of those lists as a linked list
            - ex. 1
                19 --> 9 -> 1
                9 --> 9
                point1: 9, point2: 9; sum = 18 % 10 = 8; carry = true
                point1: 1, point2: none; sum = 1 + 1 (from carry) = 2
        Plan:
            1. init point1, point2, carry, and sumHead and sumPoint
            2. sum = 0
            3. while point1 and point2:
                if carry:
                    sum = point1.val + point2.val + 1
                else:
                    sum = point1.val + point2.val
                carry = isCarry(sum)
                sumPoint.val = sum

                sumPoint.next = ListNode()
                sumPoint = sumPoint.next

                point1 = point1.next
                point2 = point2.next

            4. while point1:
                if carry:
                    sum = point1.val + 1
                else:
                    sum = point1.val
                carry = isCarry(sum)

                sumPoint.val = sum
                
        '''
        point1, point2, sumHead = l1, l2, ListNode()
        carry = False
        sumVal = 0
        sumPoint = sumHead

        while point1 or point2:
            sumVal = getPointerSum(point1, point2, carry)

            carry = isCarry(sumVal)

            sumPoint.val = sumVal % 10

            if point1:
                point1 = point1.next
            if point2:
                point2 = point2.next

            if (point1 and point2) or carry or point1 or point2:
                sumPoint.next = ListNode(1)
            
            sumPoint = sumPoint.next

            

        return sumHead




