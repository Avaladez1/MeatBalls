import time


class Slide:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if not self.head:
            self.head = Slide(data)
            self.head.next = self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            new_node = Slide(data)
            new_node.next = self.head
            current.next = new_node

    def clear(self):
        self.head = None

    def cycle(self):
        self.head = self.head.next

    def print_list(self):
        current = self.head
        while 1==1:
            print(current.data)
            current = current.next
            time.sleep(0.2)
            # if current == self.head:
                # break
    
    def __len__(self):
        int_to_return = 0
        if self.head:
            int_to_return += 1
            if self.head.next:
                current = self.head.next
                while current is not self.head:
                    int_to_return += 1
                    current = current.next
        else:
            pass
        return int_to_return

# cll = CircularLinkedList()
# for i in range(1,21):
#     cll.append(i)
# cll.print_list()
  