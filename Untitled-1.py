from random import randint

NUMBER_OF_STUDENTS = 1200
DEFAULT_DRIVE_TIME = 30

# student class by Antonio
class Student:
    def __init__(self, slides_seen, driving_time, start_time, value):
        self.slides_seen = slides_seen
        self.driving_time = driving_time
        self.start_time = start_time
        self.value = value
        self.next = None

# class Node(object):
#     def __init__(self, value):
#         self.value = value
#         self.next  = None

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
                print(front.start_time, end=" ")
                front = front.next
                print(back.start_time)
        else:
            print("Circular queue is empty !!")

    def __len__(self):
        """
        Traverse from front to back and count students
        """
        size = 0
        if self.head is not None and self.tail is not None:
            while self.tail.next != self.head:
                size += 1
                self.head = self.head.next
        return size


student_queue = LinkedCircularQueue()
arrival_times_list = []
def generate_arrival_times(list: list):
    list = []
    for i in range(NUMBER_OF_STUDENTS):
        list.append(randint(0,43200))
    list.sort()
    return list

arrival_times_list = generate_arrival_times(arrival_times_list)

for i in range(NUMBER_OF_STUDENTS):
    s = Student([], DEFAULT_DRIVE_TIME, arrival_times_list[i], 0)
    student_queue.enqueue(s)

# RUN A DAY

arrival_times_list = generate_arrival_times(arrival_times_list)

for i in range(NUMBER_OF_STUDENTS):
    if i == 0:
        s = student_queue.head
    else:
        s = s.next
    s.start_time = arrival_times_list[i]
    

student_queue.display()

