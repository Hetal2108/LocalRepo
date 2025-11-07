# -------------------------
# Node / Student Class
# -------------------------
class Student:
    def __init__(self, roll, name, marks):
        self.roll = roll
        self.name = name
        self.marks = marks
        self.next = None  # singly linked list only

# -------------------------
# Linked List Management
# -------------------------
class StudentList:
    def __init__(self):
        self.head = None

    # Add student at end
    def add(self, roll, name, marks):
        new_node = Student(roll, name, marks)
        if not self.head:
            self.head = new_node
        else:
            node = self.head
            while node.next:
                node = node.next
            node.next = new_node
        print("Student added successfully.")

    # Delete student by roll number
    def delete(self, roll):
        if not self.head:
            print("No records found.")
            return
        if self.head.roll == roll:
            self.head = self.head.next
            print("Student deleted successfully.")
            return
        node = self.head
        while node.next:
            if node.next.roll == roll:
                node.next = node.next.next
                print("Student deleted successfully.")
                return
            node = node.next
        print("Student not found.")

    # Update student by roll number
    def update(self, roll, new_name, new_marks):
        node = self.head
        while node:
            if node.roll == roll:
                node.name = new_name
                node.marks = new_marks
                print("Student updated successfully.")
                return
            node = node.next
        print("Student not found.")

    # Search student by roll number
    def search(self, roll):
        node = self.head
        while node:
            if node.roll == roll:
                print(f"Found: Roll:{node.roll}, Name:{node.name}, Marks:{node.marks}")
                return
            node = node.next
        print("Student not found.")

    # Display all students
    def display(self):
        if not self.head:
            print("No records found.")
            return
        node = self.head
        print("\nStudent Records:")
        while node:
            print(f"Roll:{node.roll}, Name:{node.name}, Marks:{node.marks}")
            node = node.next

    # Sort students (Bubble Sort)
    def sort(self, key="roll", reverse=False):
        if not self.head or not self.head.next:
            return

        swapped = True
        while swapped:
            swapped = False
            node = self.head
            while node.next:
                if key == "roll":
                    cond = node.roll > node.next.roll
                else:  # key == "marks"
                    cond = node.marks > node.next.marks

                if reverse:
                    cond = not cond

                if cond:
                    # Swap student data
                    node.roll, node.next.roll = node.next.roll, node.roll
                    node.name, node.next.name = node.next.name, node.name
                    node.marks, node.next.marks = node.next.marks, node.marks
                    swapped = True
                node = node.next
        print(f"Records sorted by {key} {'descending' if reverse else 'ascending'} order.")

# -------------------------
# Menu / Driver Code
# -------------------------
def menu():
    sl = StudentList()
    while True:
        print("\n===== Student Record Management =====")
        print("1. Add Student")
        print("2. Delete Student")
        print("3. Update Student")
        print("4. Search Student")
        print("5. Display Students")
        print("6. Sort by Roll No (Asc)")
        print("7. Sort by Roll No (Desc)")
        print("8. Sort by Marks (Asc)")
        print("9. Sort by Marks (Desc)")
        print("10. Exit")

        choice = input("Enter your choice (1-10): ")

        if choice == "1":
            roll = int(input("Enter Roll No: "))
            name = input("Enter Name: ")
            marks = float(input("Enter Marks: "))
            sl.add(roll, name, marks)

        elif choice == "2":
            roll = int(input("Enter Roll No to delete: "))
            sl.delete(roll)

        elif choice == "3":
            roll = int(input("Enter Roll No to update: "))
            name = input("Enter New Name: ")
            marks = float(input("Enter New Marks: "))
            sl.update(roll, name, marks)

        elif choice == "4":
            roll = int(input("Enter Roll No to search: "))
            sl.search(roll)

        elif choice == "5":
            sl.display()

        elif choice == "6":
            sl.sort(key="roll", reverse=False)

        elif choice == "7":
            sl.sort(key="roll", reverse=True)

        elif choice == "8":
            sl.sort(key="marks", reverse=False)

        elif choice == "9":
            sl.sort(key="marks", reverse=True)

        elif choice == "10":
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Try again.")

# Run program
menu()
