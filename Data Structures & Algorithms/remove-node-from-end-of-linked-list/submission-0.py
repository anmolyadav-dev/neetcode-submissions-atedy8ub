# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        first = head
        ct = 0
        while (first):
            first = first.next
            ct+=1
        
        index = ct - n
        ptr = head
        currNode = 0
        prev = ListNode()
        if index == 0:
            return head.next
        while (ptr):

            if currNode == index:
                prev.next = ptr.next
                break
            else:
                prev = ptr
                ptr = ptr.next
            currNode+=1
        return head
