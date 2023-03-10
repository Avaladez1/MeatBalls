import time


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if not self.head:
            self.head = Node(data)
            self.head.next = self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            new_node = Node(data)
            new_node.next = self.head
            current.next = new_node

    def print_list(self):
        current = self.head
        while 1==1:
            print(current.data)
            current = current.next
            time.sleep(0.2)
            # if current == self.head:
                # break

cll = CircularLinkedList()
for i in range(1,21):
    cll.append(i)
cll.print_list()
  