class ListNode:
    def __init__(self, value: int):
        self.value = value
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value: int) -> None:
        new_node = ListNode(value)

        if not self.head:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next

        current.next = new_node

    def to_list(self) -> list[int]:
        result = []
        current = self.head

        while current:
            result.append(current.value)
            current = current.next

        return result

    def __str__(self) -> str:
        return " -> ".join(map(str, self.to_list()))