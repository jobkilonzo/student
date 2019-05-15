student_list = []
def create_student():
    # Ask for user
    name = input("Please enter student's name: ")
    # Create dictionary
    student_data = {
        'name': name,
        'marks': []
    }
    # return the dictionary
    return student_data

def add_mark(student, mark):
    student['marks'].append(mark)

def calculate_average_mark(student):
    number = len(student['marks'])
    if number == 0:
        return 0

    total_marks = sum(student['marks'])
    return total_marks/number
def student_details(student):
    print("{}, average mark: {}".format(student['name'], calculate_average_mark(student)))

def print_lists(students):
    for i, student in enumerate(students):
        print("ID: {}".format(i))
        student_details(student)

def menu():
    selection = input("Enter p to print the student list, "
                       "'s' to add new student, "
                       "'a' to add a mark to a student, "
                       "or 'q' to quit. Enter selection: ")

    while selection != 'q':
        if selection == 'p':
            print_lists(student_list)
        elif selection == 's':
            student_list.append(create_student())
        elif selection == 'a':
            student_id = int(input("Enter student ID to add mark to: "))
            student = student_list[student_id]
            new_mark = int(input("Enter the new mark to be added: "))
            add_mark(student, new_mark)
        selection = input("Enter p to print the student list, "
                           "'s' to add new student, "
                           "'a' to add a mark to a student, "
                           "or 'q' to quit. Enter selection: ")
menu()
