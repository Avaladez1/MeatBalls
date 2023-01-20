from random import randint
from random import shuffle

NUMBER_OF_STUDENTS = 1200
DEFAULT_DRIVE_TIME = 30
DAYS = ["M", "T", "W", "R", "F"]
STUDENT_LIST = []

# student class by Antonio
class Student:
    def __init__(self):
        self.slides_seen = []
         # TODO randomize driving time between 15-25 seconds maybe 
        self.driving_time = DEFAULT_DRIVE_TIME
        self.next = None
        #random with weights to prioritize 2&3
        number_of_days = randint(1,5)
        #random with weights to prioritize MWF if 3, TR if 2.
        self.days = ["M", "T", "W", "R", "F"]
        shuffle(self.days)
        self.days = self.days[0:number_of_days]
        self.arrival_times = []
        average_arrival = randint(0,43200)
        for i in range(len(self.days)):
            self.arrival_times.append(randint(-600,600)+average_arrival)
        self.schedule = dict(zip(self.days, self.arrival_times))

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
        return self.tail.arrival_times

    def dequeue(self):
        """
        Remove the oldest node (from the front) by copying the value and
        making the preceding node as the new head
        """
        if self.head is not None:
            deleted = self.head.arrival_times
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
                print(front.schedule, end="\n")
                front = front.next
                #print(back.schedule)
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
    s = Student()
    STUDENT_LIST.append(s)

# RUN A DAY
# (this is just an example)
mondays = 0
for student in STUDENT_LIST:
    if "M" in student.schedule:
        student_queue.enqueue(student)
        mondays += 1

        

arrival_times_list = generate_arrival_times(arrival_times_list)

for i in range(NUMBER_OF_STUDENTS):
    if i == 0:
        s = student_queue.head
    else:
        s = s.next
    s.start_time = arrival_times_list[i]
    
student_queue.display()

print(mondays)