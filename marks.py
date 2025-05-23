# Student Marks Manager (Real-Time Console App)
# It allows:
# Adding students and their marks
# Viewing all students
# Calculating average
# Searching
# Updating
# Exiting
# ---------- GLOBAL DATA ----------
students = []  # List of tuples (name, [marks])

# ---------- FUNCTIONS ----------

def add_student():
    name = input("Enter student name: ").strip()
    marks = []
    for i in range(3):
        mark = int(input(f"Enter mark {i + 1}: "))
        marks.append(mark)
    students.append((name, marks))
    print(f"\n✅ {name} added successfully!\n")

def view_students():
    if not students:
        print("❌ No students yet.\n")
        return
    print("\n📋 All Students:")
    for i, (name, marks) in enumerate(students):
        print(f"{i + 1}. {name} - Marks: {marks} - Avg: {sum(marks)/len(marks):.2f}")
    print()

def search_student():
    search = input("Enter student name to search: ").strip()
    found = False
    for name, marks in students:
        if name.lower() == search.lower():
            print(f"\n🎯 Found: {name} - Marks: {marks} - Avg: {sum(marks)/len(marks):.2f}\n")
            found = True
    if not found:
        print("❌ Student not found!\n")

def update_student():
    name_to_update = input("Enter student name to update: ").strip()
    for i in range(len(students)):
        name, marks = students[i]
        if name.lower() == name_to_update.lower():
            print(f"📢 Updating {name}")
            new_marks = []
            for j in range(3):
                new_mark = int(input(f"Enter new mark {j + 1}: "))
                new_marks.append(new_mark)
            students[i] = (name, new_marks)
            print(f"✅ {name} updated.\n")
            return
    print("❌ Student not found!\n")

def average_class_marks():
    if not students:
        print("❌ No students to calculate average.\n")
        return
    total = 0
    count = 0
    for _, marks in students:
        total += sum(marks)
        count += len(marks)
    print(f"\n📊 Class Average Marks: {total / count:.2f}\n")

def show_menu():
    print("======== Student Marks Manager ========")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Update Student Marks")
    print("5. Class Average")
    print("6. Exit")
    print("=======================================\n")

# ---------- MAIN LOOP ----------
while True:
    show_menu()
    choice = input("Enter your choice (1–6): ")

    if choice == '1':
        add_student()
    elif choice == '2':
        view_students()
    elif choice == '3':
        search_student()
    elif choice == '4':
        update_student()
    elif choice == '5':
        average_class_marks()
    elif choice == '6':
        print("👋 Exiting... Goodbye!")
        break
    else:
        print("❌ Invalid choice! Please try again.\n")
