import student_queue as sq
import linked_list as ll
from math import ceil
import statistics as stat

STUDENT_LIST = []
number_of_students = 1200
slide_length = 20
number_of_slides = 20

# create queue
student_queue = sq.LinkedCircularQueue()

# generate students (not yet in queue, but in student master list)
sq.generate_students(STUDENT_LIST, number_of_students)

# create sign
sign = ll.CircularLinkedList()

# DAY SIMULATION FUNCTIONS ---------------------------------------------

def queue_day(day: str):
    students_to_enqueue = []
    for student in STUDENT_LIST:
        if day in student.schedule:
            students_to_enqueue.append(student)
    students_to_enqueue.sort(key = lambda x: x.schedule[day])
    # generate random driving times for the day
    daily_driving_times = sq.generate_driving_times(students_to_enqueue)
    index_counter = 0
    for student in students_to_enqueue:
        student.driving_time = daily_driving_times[index_counter]
        student_queue.enqueue(student)
        index_counter += 1

def simulate_day(day: str):
    # timer runs from 0 (6:00 AM) to 44400 (6:20 PM) so that no students arrive after the day ends or before the day starts
    timer = 0
    while timer <= 50000:
        # cycle the sign every 20 "seconds"
        if timer % slide_length == 0:
            sign.cycle()
        # FIRST, check if the queue head exists (if the queue is not empty), THEN, check the head's schedule
        # The order of the AND matters, because python will only do check until it finds a false, and then the rest of the true/false statements will not get checked
        # if it checks the schedule of the head first, when there is no head, you get a NoneType error
        while student_queue.head and timer == student_queue.head.schedule[day]:
            # The following is an expanded equation to look into the future to see how many slides a student SHOULD see.
            # how long the slide has already run before the student arrived
            current_slide_ellapsed_time = student_queue.head.schedule[day] % slide_length
            # how long the student will see their first slide 
            current_slide_remaining_time = slide_length - current_slide_ellapsed_time
            # how much time remains after the student's first slide cycles
            time_to_see_additional_slides = student_queue.head.driving_time - current_slide_remaining_time
            # number of slides a student should see
            number_of_slides_to_see = ceil(time_to_see_additional_slides / slide_length) + 1
            # print(f"arrival time: {student_queue.head.schedule[day]}")
            # print(f"driving time: {student_queue.head.driving_time}")
            # print(f"slides seen: {number_of_slides_to_see}")
            current_slide = sign.head
            for i in range(number_of_slides_to_see):
                if current_slide not in student_queue.head.slides_seen:
                    student_queue.head.slides_seen.append(current_slide)
                current_slide = current_slide.next
            student_queue.dequeue()
        timer += 1
    # clearing the queue should be redundant, but i'm doing it anyway to avoid taking any chances
    student_queue.clear()

def elim_duplicates(slides:list):
    """
    Takes the list that it is given and turns it into a dictionary. This eliminates duplicate keys, and the result is turned back into a list and printed.
    """
    Slides_seen = list(dict.fromkeys(slides))
    # print(student.driving_time, Slides_seen.value)

def simulate_week():
    # put slides in the sign
    sign.clear()
    for i in range(1, number_of_slides+1):
        sign.append(i)
    # reset student list with updated number of students
    sq.generate_students(STUDENT_LIST, number_of_students)
    for day in sq.DAYS:
        queue_day(day)
        # print(len(student_queue))
        simulate_day(day)
        # student_queue.display()
    for student in STUDENT_LIST:
        # print(f"Driving time:{student.driving_time}  Arrival times:{student.arrival_times}  Slides seen:{student.slides_seen}")
        # Prints the final lists of slides seen
        elim_duplicates(student.slides_seen)
    
# RESULTS FUNCTIONS ---------------------------------------

def average_students_that_saw_slide(list: list, circular: ll.CircularLinkedList):
    """
    TAKES: list of students, list of slides.
    Prints "Slide X was seen by N% of students." for each slide
    """
    percentages = []
    for i in range(len(sign)):
        slide_sightings = 0
        for student in list:
            if circular.head in student.slides_seen:
                slide_sightings += 1
        percentages.append(slide_sightings / len(list))
        circular.cycle()
    string_to_return = ""
    for i in range(len(percentages)):
        # print(f"Slide #{i+1} was seen by {percentages[i]*100}% of students.")
        string_to_return += f"Slide #{i+1} was seen by {percentages[i]*100}% of students.\n"
    return string_to_return

def percentage_of_slides_seen(student: sq.Student) -> float:
    percentage = (len(student.slides_seen) / slide_length) * 100
    return percentage

def oble(list_of_students: list):
    percentages_list = []
    for student in list_of_students:
        percentages_list.append(percentage_of_slides_seen(student))
    print(f"The average student saw {stat.mean(oble)}% of the slides.")



# Example usage
# simulate_week()
# average_students_that_saw_slide(STUDENT_LIST, sign)