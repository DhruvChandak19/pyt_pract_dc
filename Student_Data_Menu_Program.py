students = ["Aman", "Riya", "Neha", "Kunal"]
subjects = ("Maths", "Physics", "Chemistry", "Computer Science")
marks = {"Aman": 82, "Riya": 91, "Neha": 76, "Kunal": 88}
unique_values = (7.5, 8.9, 6.8, 8.2)

while True:
    print("\n1. Students")
    print("2. Subjects")
    print("3. Marks")
    print("4. Unique Values")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        print(students)
    elif choice == "2":
        print(subjects)
    elif choice == "3":
        print(marks)
    elif choice == "4":
        print(unique_values)
    elif choice == "5":
        break
    else:
        print("Wrong choice")
