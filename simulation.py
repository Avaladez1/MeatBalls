import student_queue as sq
import linked_list as ll

STUDENT_LIST = []
NUMBER_OF_STUDENTS = 1200
SLIDE_LENGTH = 20

# create queue

# generate students (not yet in queue, but in student master list)
sq.generate_students(STUDENT_LIST, 1200)

# create sign
sign = ll.CircularLinkedList()
# put slides in the sign
for i in range(1, 21):
    sign.append(i)

# DAY SIMULATION FUNCTIONS

def queue_day(day: str):
    students_to_enqueue = []
    for student in STUDENT_LIST:
        if day in student.schedule:
            students_to_enqueue.append(student)
            students_to_enqueue.sort(key = lambda x: x.schedule[day])
    for student in students_to_enqueue:
        student_queue.enqueue(student)

def simulate_day(day: str):
    timer = 0
    while timer <= 43200:
        # cycle the sign every 20 "seconds"
        if timer % SLIDE_LENGTH == 0:
            sign.cycle()
        # when the student arrives, if they haven't already seen the current slide, append it to their slides_seen list
        while timer == student_queue.head.schedule[day]:
            if sign.head.data not in student_queue.head.slides_seen:
                student_queue.head.slides_seen.append(sign.head.data)
            if student_queue.head.schedule[day] % SLIDE_LENGTH < student_queue.head.driving_time-SLIDE_LENGTH:
                student_queue.head.slides_seen.append(sign.head.next.data)
            else:
                student_queue.head.slides_seen.append(sign.head.next.data)
                student_queue.head.slides_seen.append(sign.head.next.next.data)
            student_queue.dequeue()
        timer += 1

def elim_duplicates(slides:list):
    """
    Takes the list that it is given and turns it into a dictionary. This eliminates duplicate keys, and the result is turned back into a list and printed.
    """
    Slides_seen = list(dict.fromkeys(slides))
    print(student.driving_time, Slides_seen)
    
# RESULTS FUNCTIONS

def average_students_that_saw_slide(list: list, circular: ll.CircularLinkedList):
    temp_list = []
    

for day in sq.DAYS:
    student_queue = sq.LinkedCircularQueue()
    queue_day(day)
    simulate_day(day)
    # student_queue = None
    student_queue.display()


for student in STUDENT_LIST:
    # Prints the final lists of slides seen
    elim_duplicates(student.slides_seen)

def percentage_of_slides_seen(student: sq.Student) -> float:
    percentage = (len(student.slides_seen) / SLIDE_LENGTH) * 100
    return percentage

# Example usage
for student in STUDENT_LIST:
    print(f"{student} has seen {percentage_of_slides_seen(student)}% of the slides.")
