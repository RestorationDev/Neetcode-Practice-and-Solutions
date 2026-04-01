# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        carry = 0
        cur = dummy
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            #adds prev carry value in add'n to sum
            added = val1 + val2 + carry
            #if any carry will calculate 10s place digit
            carry = added // 10
            #added just becomes the ones place by applying remainder oper'n
            added = added % 10
            cur.next = ListNode(added)
            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        return dummy.next
        

        

        