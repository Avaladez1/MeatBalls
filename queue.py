class Node(object):
    def __init__(self, value):
        self.value = value
        self.next  = None

class LinkedCircularQueue(object):
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail

    def enqueue(self, item):
        """
        Add the node to the back of the queue and set its next pointer to
        self.head
        """
        if self.tail is not None:
            self.tail.next = item
        else:
            self.head = item

        self.tail = item
        item.next = self.head
        return self.tail.value

    def dequeue(self):
        """
        Remove the oldest node (from the front) by copying the value and
        making the preceding node as the new head
        """
        if self.head is not None:
            deleted = self.head.value
            self.head = self.head.next
        else:
            deleted = None
            print("Circular queue is empty !!")
        return deleted

    def display(self):
        """
        Traverse from front to back and show students
        """
        front = self.head
        back  = self.tail
        if front is not None and back is not None:
            while back != front:
                print(front.value, end=" ")
                front = front.next
                print(back.value)
        else:
            print("Circular queue is empty !!")

    def get_size(self):
        """
        Traverse from front to back and count students
        """
        size = 0
        if self.head is not None and self.tail is not None:
            while self.tail.next != self.head:
                size += 1
                self.head = self.head.next
        return size

def main():
    # Initialize students
    student1 = Node(1)
    student2 = Node(2)
    student3 = Node(3)
    student4 = Node(4)
    student5 = Node(5)
    linked_circular_queue = LinkedCircularQueue()

    # Initial tests
    linked_circular_queue.display()
    print(linked_circular_queue.is_empty())
    print(linked_circular_queue.get_size())
    print()

    # Test enqueue
    linked_circular_queue.enqueue(student5)
    linked_circular_queue.enqueue(student3)
    linked_circular_queue.enqueue(student1)
    linked_circular_queue.enqueue(student4)
    linked_circular_queue.enqueue(student2)
    linked_circular_queue.display()             # doesn't work
    print()

    # Test dequeue
    linked_circular_queue.dequeue()
    linked_circular_queue.dequeue()
    linked_circular_queue.display()
    print()

    # Test peek
    print(linked_circular_queue.peek_front())
    print(linked_circular_queue.peek_back())
    print()

    # Final tests
    print(linked_circular_queue.is_empty())
    print(linked_circular_queue.get_size())

main()
