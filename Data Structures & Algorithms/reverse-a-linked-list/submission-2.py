
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

#in this solution, we have prev, curr, next_
#for the logic at the middle/end of the list, 
#first set next_ to curr.next
#then set curr.next to prev
#then assign curr to next and prev to curr
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        #to reverse it we start at the head and set the next to none, and as we get to the next node
        # do the following
        # set the current.next to the previous element, store the actual next so we can get to it next,
        # and then rinse and repeat, until we actually are at the end


        prev = None
        current = head
        next_elem = None

        while current:

            next_elem = current.next
            current.next = prev
            prev = current
            current = next_elem
        
        return prev
        