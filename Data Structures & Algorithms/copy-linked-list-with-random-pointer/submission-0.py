
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        '''
        Understand:
            copyRandomList: [Head of Linkedlist with random] -> [Head of LinkedList with Random]
            goal: given linked list of ints with next and random pointer return a deep copy of given linked list
            ex 1:  [3, null] -> [7, 3] -> [4, 0] -> [5, 1] -> null return copy
                {
                    Node(3, Node(7), null): Node(3)
                    Node(7, Node(4), Node(5)): Node(7)
                    Node(4, Node(5), Node(3)): Node(4)
                    Node(5, null, Node(7)): Node(5)
                },
                Wire up node field values 
        Plan:
            Multi-pass technique
            first pass create dict that contains Node copies
            second pass, wire up node copies
            return dict[curr]
        '''
        curr = head
        currToCopy = {None: None}

        while curr:
            currToCopy[curr] = Node(curr.val)
            curr = curr.next
        
        curr = head
        while curr:
            currToCopy[curr].next = currToCopy[curr.next]
            currToCopy[curr].random = currToCopy[curr.random]
            curr = curr.next
        
        curr = head
        return currToCopy[curr]


