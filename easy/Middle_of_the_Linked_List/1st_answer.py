# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        tmp_head = head
        count = 0
        while True:
            if head.next != None:
                count += 1
                head = head.next
            else:
                count += 1
                break
        head = tmp_head
        for i in range(int(count/2)):
            head = head.next
        return head
