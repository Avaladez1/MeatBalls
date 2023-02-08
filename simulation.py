import student_queue as sq
import linked_list as ll
from math import ceil

STUDENT_LIST = []
NUMBER_OF_STUDENTS = 1200
SLIDE_LENGTH = 2

# create queue

# generate students (not yet in queue, but in student master list)
sq.generate_students(STUDENT_LIST, NUMBER_OF_STUDENTS)

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
            # if sign.head.data not in student_queue.head.slides_seen:
            #     student_queue.head.slides_seen.append(sign.head.data)
            # slides_to_see = ceil(((student_queue.head.schedule[day] + student_queue.head.driving_time) % SLIDE_LENGTH) / SLIDE_LENGTH) + 1
            # how long the slide has already run before the student arrived
            current_slide_ellapsed_time = student_queue.head.schedule[day] % SLIDE_LENGTH
            # how long the student will see their first slide 
            current_slide_remaining_time = SLIDE_LENGTH - current_slide_ellapsed_time
            # how much time remains after the student's first slide cycles
            time_to_see_additional_slides = student_queue.head.driving_time - current_slide_remaining_time
            # number of slides a student should see
            number_of_slides_to_see = ceil(time_to_see_additional_slides / SLIDE_LENGTH) + 1
            print(f"arrival time: {student_queue.head.schedule[day]}")
            print(f"driving time: {student_queue.head.driving_time}")
            print(f"slides seen: {number_of_slides_to_see}")
            current_slide = sign.head
            for i in range(number_of_slides_to_see):
                if current_slide not in student_queue.head.slides_seen:
                    student_queue.head.slides_seen.append(current_slide)
                current_slide = current_slide.next
            # if student_queue.head.schedule[day] % SLIDE_LENGTH < abs(student_queue.head.driving_time-SLIDE_LENGTH):
            #     student_queue.head.slides_seen.append(sign.head.next.data)
            # else:
            #     student_queue.head.slides_seen.append(sign.head.next.data)
            #     student_queue.head.slides_seen.append(sign.head.next.next.data)
            student_queue.dequeue()
        timer += 1

def elim_duplicates(slides:list):
    """
    Takes the list that it is given and turns it into a dictionary. This eliminates duplicate keys, and the result is turned back into a list and printed.
    """
    Slides_seen = list(dict.fromkeys(slides))
    # print(student.driving_time, Slides_seen.value)
    
# RESULTS FUNCTIONS

def average_students_that_saw_slide(list: list, circular: ll.CircularLinkedList):
    percentages = []
    for i in range(len(sign)):
        slide_sightings = 0
        for student in list:
            if circular.head.data in student.slides_seen:
                slide_sightings += 1
        percentages.append(slide_sightings / len(list))
        circular.cycle()
    for i in range(len(percentages)):
        print(f"Slide #{i+1} was seen by {percentages[i]*100}% of students.")

for day in sq.DAYS:
    student_queue = sq.LinkedCircularQueue()
    queue_day(day)
    simulate_day(day)
    # student_queue = None
    student_queue.display()


for student in STUDENT_LIST:
    print(f"Driving time:{student.driving_time}  Arrival times:{student.arrival_times}  Slides seen:{student.slides_seen}")
    # Prints the final lists of slides seen
    elim_duplicates(student.slides_seen)

def percentage_of_slides_seen(student: sq.Student) -> float:
    percentage = (len(student.slides_seen) / SLIDE_LENGTH) * 100
    return percentage

import statistics as s
# Example usage
oble = []
for student in STUDENT_LIST:
    oble.append(percentage_of_slides_seen(student))
print(f"{student} average {s.mean(oble)}% of the slides.")

average_students_that_saw_slide(STUDENT_LIST, sign)