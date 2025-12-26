from linked_list import ListNode

def merge_sorted_lists(l1: ListNode | None, l2: ListNode | None) -> ListNode | None:

    dummy = ListNode(0)
    tail = dummy

    while l1 and l2:
        if l1.value < l2.value:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next

    tail.next = l1 if l1 else l2

    return dummy.next