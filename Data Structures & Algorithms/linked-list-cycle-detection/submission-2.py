# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# we set a slow and fast ptr where slow (1 step) and fast (2 step)
# cycle if there is overlap...

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast = head
        slow = head
        
        while fast and slow:
            if slow.next:
                slow = slow.next
            else:
                break
            
            if fast.next and fast.next.next:
                fast = fast.next.next 
            else:
                break

            if slow == fast:
                return True
        return False
            

        