# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# we set a slow and fast ptr where slow (1 step) and fast (2 step)
# cycle if there is overlap...

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        #cycle if node is revisited (i.e. later node points to it)
        #index, not given, determines loacation of cycle beginning
        #we know that we use fast/slow ptr for the problem
        
        slow = head
        fast = head

        while fast and fast.next:

            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
        
        return False
            

        