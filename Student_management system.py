# Project Question: Student Management System (OOP & Encapsulation)
# Develop a Student Management System using Python that demonstrates the concepts of Object-Oriented Programming (OOP) and Encapsulation.
#  Requirements:
# 1. 	Create a Student class with the following:
# o   name as a public data member
# o   student_id as a private data member
# o   marks as a private data member
# 2. 	Implement the following methods in the Student class:
# o   A constructor to initialize student details
# o   Getter methods to access:
# § Student ID
# § Marks
# o   A setter method to update marks with validation (marks should be between 0 and 100)
# o   A method to display student details
# 3. 	Maintain a list to store multiple student objects.
# 4. 	Implement menu-driven functions to:
# o   Add a new student# Project Question/ Student Management S
# o   View all students
# o   Search for a student using student ID
# o   Update student details (name and marks)
# o   Delete a student using student ID
# 5. 	Ensure:
# o   Direct access to private data members is restricted
# o   All updates to marks are done using setter methods
# o   Proper messages are displayed for invalid operations
# 6. 	The program should continue running until the user chooses to exit.

from datetime import date
today=date.today()
print("today".center(50)) 
print(50 * '-')
print("Welcome To Student Management System".center(50))
print(50 * '-')

class Student:
    def __init__(self, name, student_id, marks):
        self.name = name
        self.__student_id = student_id
        self.__marks = marks

    def get_student_id(self):
        return self.__student_id

    def get_marks(self):
        return self.__marks

    def set_marks(self, marks):
        if 0 <= marks <= 100:
            self.__marks = marks
        else:
            raise Exception("Marks should be between 0 and 100")

    def display(self):
        print("Name:", self.name)
        print("Student ID:", self.__student_id)
        print("Marks:", self.__marks)
        print("-" * 30)


student_list = []

def add_student():
    try:
        name = input("Enter student name: ")
        student_id = input("Enter student ID: ")
        marks = int(input("Enter marks: "))
        student_list.append(Student(name, student_id, marks))
        print("Student added successfully")
    except Exception as e:
        print("Invalid input:", e)

def view_all_students():
    if not student_list:
        print("No students available")
        return
    for student in student_list:
        student.display()

def search_student():
    std_id = input("Enter student ID to search: ")
    for student in student_list:
        if student.get_student_id() == std_id:
            print("Student found")
            student.display()
            return
    print("Student not found")

def update_student():
    std_id = input("Enter student ID to update: ")
    for student in student_list:
        if student.get_student_id() == std_id:
            student.name = input("Enter new name: ")
            try:
                new_marks = int(input("Enter new marks: "))
                student.set_marks(new_marks)
                print("Student updated successfully")
            except Exception as e:
                print("Error:", e)
            return
    print("Student not found")

def delete_student():
    std_id = input("Enter student ID to delete: ")
    for student in student_list:
        if student.get_student_id() == std_id:
            student_list.remove(student)
            print("Student deleted successfully")
            return
    print("Student not found")


while True:
    print("""
1. Add Student
2. View All Students
3. Search Student
4. Update Student
5. Delete Student
6. Exit
""")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_all_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        update_student()
    elif choice == "5":
        delete_student()
    elif choice == "6":
        print("Exiting Student Management System")
        break
    else:
        print("Invalid choice")



