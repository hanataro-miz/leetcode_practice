# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        tmp_lists = [l1, l2]
        val_list = []
        next = 0
        longer = 0
        while l1 != None or l2 != None:
            if l1 == None:
                tmp = l2.val + next
                l2 = l2.next
                longer = 1
            elif l2 == None:
                tmp = l1.val + next
                l1 = l1.next
                longer = 0
            else:
                tmp = l1.val + l2.val + next
                l1 = l1.next
                l2 = l2.next
            if tmp >= 10:
                next = 1
                tmp -= 10
            else:
                next = 0
            val_list.append(tmp)
        
        l1 = tmp_lists[longer]
        i = 0
        while l1 != None:
            l1.val = val_list[i]
            i += 1
            l1 = l1.next
            
        if next == 1:
            new_Node = ListNode()
            new_Node.val = 1
            l1 = tmp_lists[longer]
            while l1.next != None:
                l1 = l1.next
            l1.next = new_Node
        l1 = tmp_lists[longer]
        return l1

# Runtime: 96 ms, faster than 61.80% of Python3 online submissions for Add Two Numbers.
# Memory Usage: 14 MB, less than 10.33% of Python3 online submissions for Add Two Numbers.
