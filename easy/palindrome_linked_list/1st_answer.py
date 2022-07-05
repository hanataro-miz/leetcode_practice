# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        order_list = []
        i = 0
        while True:
            order_list.append(head.val)
            if head.next == None:
                break
            head = head.next
            i += 1
        reverse_list = list(reversed(order_list))
        for i in range(len(order_list)):
            if order_list[i] != reverse_list[i]:
                return False
        return True
