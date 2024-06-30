def delete_node(self, head, x):
    if head is None:
        return None

    current = head
    for _ in range(x - 1):
        if current is None:
            return head
        current = current.next

    if current is head:
        head = current.next
        if head:
            head.prev = None
    else:
        if current.next:
            current.next.prev = current.prev
        if current.prev:
            current.prev.next = current.next

    return head
