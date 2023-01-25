import student_queue as sq
import linked_list as ll

STUDENT_LIST = []
NUMBER_OF_STUDENTS = 200
SLIDE_LENGTH = 20

# create queue
student_queue = sq.LinkedCircularQueue()
# generate students (not yet in queue, but in student master list)
sq.generate_students(STUDENT_LIST, 1200)

# create sign
sign = ll.CircularLinkedList()
# put slides in the sign
for i in range(1, 21):
    sign.append(i)

# MONDAY

students_to_enqueue = []
for student in STUDENT_LIST:
    if "M" in student.schedule:
        students_to_enqueue.append(student)
        students_to_enqueue.sort(key = lambda x: x.schedule["M"])
for student in students_to_enqueue:
    student_queue.enqueue(student)

timer = 0
while timer <= 43200:
    # cycle the sign every 20 "seconds"
    if timer % SLIDE_LENGTH == 0:
        sign.cycle()
    # when the student arrives, if they haven't already seen the current slide, append it to their slides_seen list
    while timer == student_queue.head.schedule["M"]:
        if sign.head.data not in student_queue.head.slides_seen:
            student_queue.head.slides_seen.append(sign.head.data)
        student_queue.dequeue()

    # sleep(0.01)
    timer += 1
for student in STUDENT_LIST:
    print(student.slides_seen)
