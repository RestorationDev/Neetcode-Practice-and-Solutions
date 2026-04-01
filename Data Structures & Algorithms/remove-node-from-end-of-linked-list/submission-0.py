# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #essentially remove the nth node incrementing from the end of the LL

        curr = head 

        node = None

        while curr:
            tmp = curr.next
            curr.next = node
            node = curr
            curr = tmp
        

        pos = 1
        while node:
            #print(node.val)
            if pos == n:
                node = node.next
                pos += 1
                continue
            print(node.val)
            temp = node.next
            node.next = curr
            curr = node
            node = temp

            pos += 1
        
        return curr