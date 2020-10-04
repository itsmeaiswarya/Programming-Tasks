#definition for singly - linked list
class ListNode:
    def __init__(self, data):
        self.data = data
        self.link = None

def hasCycle(head:ListNode) -> bool:
    """initialize slow & fast ptr to head node"""
    slow = head
    fast = head
    """traverse the linked list"""
    while fast!= None and fast.link!= None:
        """increment slow by one node"""
        slow = slow.link
        """increment fast by two nodes"""
        fast = fast.link.link
        """if slow & fast meet then loop found, return true"""
        if slow == fast:
            return True
    """if slow & fast don't meet there is no loop return false"""
    return False

if __name__ == "__main__":
    head = ListNode(1)
    head.link = l1 = ListNode(2)
    l1.link = l2 = ListNode(4)
    l2.link = l3 = ListNode(16)
    l3.link = l4 = ListNode(10)
    l4.link = l2
    """1->2->4->16->10--|
             |__________|"""
    print(hasCycle(head))