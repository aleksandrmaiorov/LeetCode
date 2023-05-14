##Feel free to use this code.
## OpenSource Rulez

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        curr = head
        while(curr and curr.next):
            if curr.val == curr.next.val:
                temp = curr.next
                curr.next = temp.next
            else:
                curr = curr.next
        return head
