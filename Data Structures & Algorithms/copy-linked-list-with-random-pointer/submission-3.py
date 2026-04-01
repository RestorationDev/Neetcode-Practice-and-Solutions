
# Definition for a Node.
# class Node:
#     def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
#         self.val = int(x)
#         self.next = next
#         self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        #create a dummy node and every new node (using next) create ListNode() with relevant info
        #edge case: random node isn't created yet, in this case, also create a list node, but if it already exists might want to store it in case

        #let's try implementing by iterating and creating a copy of each node
        
        oldToCopy = {None:None}

        curr = head

        while curr:
            copy = Node(curr.val)
            oldToCopy[curr] = copy
            curr = curr.next

        curr = head

        while curr:
            copy = oldToCopy[curr]
            copy.next = oldToCopy[curr.next]
            copy.random = oldToCopy[curr.random]
            curr = curr.next
        
        return oldToCopy[head]
        


        


        