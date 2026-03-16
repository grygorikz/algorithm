def count(self):
    count = 0
    current = self.head
    while current:
        count += 1
        current = current.next
    return count