# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        '''
        Understand:
            - removeNthFromEnd: [Linked List of ints] [int] -> [LinkedList]
            - goal: given linked list and n, remove the nth node (starting from end of the list)
            - ex. 5 n=1 --> none
                - point1: 5, dummy: None -> 5
        Plan:
            1. Get size of linked list
            2. Set the target position to be size - n + 1
            3. Iterate while pos < target::
                - traverse pointers
            4. Set the behind.next = front.next
        '''
        length = 0
        current = head
        while current:
            length += 1
            current = current.next
        
        target = length - n + 1

        pos = 1
        behind = None
        front = head
        while pos < target:
            behind = front
            front = front.next
            pos += 1
        
        if behind:
            behind.next = front.next
        else:
            return front.next
        return head



