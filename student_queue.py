from random import randint, shuffle, choices

# DEFAULT_DRIVE_TIME = 30
DAYS = ["M", "T", "W", "R", "F"]
NUMBERS = [1, 2, 3, 4, 5]
#Blocks of time where students come; Weighted (6:20,8,9:40,11:20,1:00,2:40,4:20,6, [randomtime])
TIME_BLOCKS = [1200,7200,13200,19200,25200,31200,37200,43200,0]


# student class by Antonio
class Student:
    def __init__(self):
        self.slides_seen = []
         # TODO randomize driving time between 15-25 seconds maybe 
        self.driving_time = randint(20, 30)
        self.next = None
        #random with weights to prioritize 2&3
        self.number_of_days = choices(NUMBERS, weights=(1, 4, 4, 2, 1), k=1)[0]
        # print(self.number_of_days)
        #random with weights to prioritize MWF if 3, TR if 2.

        day_choices = ["M", "T", "W", "R", "F"]

        # self.days = ["M", "T", "W", "R", "F"]
        self.days = []


        for i in range (self.number_of_days):
            if self.number_of_days == 1:
                self.days.append(choices(day_choices, weights = (10,10,10,10,10), k = 1)[0])
            elif self.number_of_days == 2:
                self.days.append(choices(day_choices, weights = (10,50,10,50,10), k = 1)[0])
                if "T" in self.days:
                    self.days.append(choices(day_choices, weights = (10,0,10,50,10), k = 1)[0])
                elif "R" in self.days:
                    self.days.append(choices(day_choices, weights = (10,50,10,0,10), k = 1)[0])
            elif self.number_of_days == 3:
                self.days.append(choices(day_choices, weights = (50,10,50,10,50), k = 1)[0])
                if "M" in self.days:
                    self.days.append(choices(day_choices, weights = (0,10,50,10,50), k = 1)[0])
                elif "W" in self.days:
                    self.days.append(choices(day_choices, weights = (50,10,0,10,50), k = 1)[0])
                elif "F" in self.days:
                    self.days.append(choices(day_choices, weights = (50,10,50,10,0), k = 1)[0])
            elif self.number_of_days == 4:
                self.days.append(choices(day_choices, weights = (50,50,50,50,10), k = 1)[0])
                if "M" in self.days:
                    self.days.append(choices(day_choices, weights = (0,50,50,50,10), k = 1)[0])
                elif "T" in self.days:
                    self.days.append(choices(day_choices, weights = (50,0,50,50,10), k = 1)[0])
                elif "W" in self.days:
                    self.days.append(choices(day_choices, weights = (50,50,0,50,10), k = 1)[0])
                elif "R" in self.days:
                    self.days.append(choices(day_choices, weights = (50,50,50,0,10), k = 1)[0])
                elif "F" in self.days:
                    self.days.append(choices(day_choices, weights = (50,50,50,50,0), k = 1)[0])
            elif self.number_of_days == 5:
                self.days = ["M", "T", "W", "R", "F"]

        self.days = list(dict.fromkeys(self.days))

        # shuffle(self.days)
        # self.days = self.days[0:self.number_of_days]
        self.arrival_times = []
        average_arrival = choices(TIME_BLOCKS, weights=(1,2,5,5,5,3,3,1,1), k=1)[0]


        for i in range(len(self.days)):
            if average_arrival in TIME_BLOCKS and average_arrival != 0:
                self.arrival_times.append(randint(-1199,1200)+average_arrival)
            else:
                self.arrival_times.append(randint(0,43200))


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


# student_queue = LinkedCircularQueue()
# arrival_times_list = []
# def generate_arrival_times(list: list):
#     list = []
#     for i in range(NUMBER_OF_STUDENTS):
#         list.append(randint(0,43200))
#     list.sort()
#     return list

# arrival_times_list = generate_arrival_times(arrival_times_list)

def generate_students(list: list, i: int):
    for n in range(i):
        s = Student()
        list.append(s)

# RUN A DAY
# (this is just an example)
# mondays = 0
# for student in STUDENT_LIST:
#     if "M" in student.schedule:
#         student_queue.enqueue(student)
#         mondays += 1

        

# arrival_times_list = generate_arrival_times(arrival_times_list)

# for i in range(NUMBER_OF_STUDENTS):
#     if i == 0:
#         s = student_queue.head
#     else:
#         s = s.next
#     s.start_time = arrival_times_list[i]
    