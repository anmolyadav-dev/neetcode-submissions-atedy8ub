# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast = head.next
        slow = head
        
        while fast and fast.next :

            fast = fast.next.next
            slow = slow.next;
        temp = slow
        slow = slow.next
        temp.next = None
        prev = None
        
        while slow :
            
            nextNode = slow.next
            slow.next = prev
            prev = slow
            slow= nextNode
        # print(prev.val,prev.next.val)
        left = head
        right = prev
        # print(slow.val)
        while right and left :
            nextLeft = left.next
            nextRight = right.next
            left.next = right
            right.next = nextLeft
            
            left = nextLeft
            right = nextRight
            
            
         
        


        
        