from .node import ListNode
from .merge_lists import merge_sorted_lists

def get_middle(head: ListNode) -> ListNode:
    slow = head
    fast = head.next

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow

def merge_sort(head: ListNode | None) -> ListNode | None:
    if not head or not head.next:
        return head

    middle = get_middle(head)
    right_head = middle.next
    middle.next = None  # разрываем список

    left_sorted = merge_sort(head)
    right_sorted = merge_sort(right_head)

    return merge_sorted_lists(left_sorted, right_sorted)