# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # want a prev for the previous element, set that to the next one and a placeholder so we know where to advance

        prev = None
        curr = head

        while curr:
            nextElem = curr.next
            curr.next = prev
            prev = curr
            curr = nextElem
        return prev