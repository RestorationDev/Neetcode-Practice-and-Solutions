
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
        
        prev = None
        current = head

        while current:

            next_ = current.next
            current.next = prev
            prev = current
            current = next_
        return prev
