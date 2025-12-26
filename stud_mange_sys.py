students = []

while True:
    print("\n1.Add  2.View  3.Search  4.Update  5.Delete  6.Exit")
    choice = input("Enter your choice: ")

    if choice not in ['1','2','3','4','5','6']:
        print("Invalid choice. Please try again.")
        continue

    elif choice == '1':
        row = []
        id = input("Enter Student ID: ")
        name = input("Enter Student Name: ")
        age = int(input("Enter Student Age: "))
        course = input("Enter Student Course: ")
        marks = int(input("Enter Student Marks: "))

        row.extend([id, name, age, course, marks])
        students.append(row)

        print("Student added successfully!")

    elif choice == '2':
        if not students:
            print("No students available.")
        else:
            print("ID\tName\tAge\tCourse\tMarks")
            for s in students:
                print(f"{s[0]}\t{s[1]}\t{s[2]}\t{s[3]}\t{s[4]}")

    elif choice == '3':
        search_name = input("Enter the student name to search: ")
        found = False

        print("ID\tName\tAge\tCourse\tMarks")
        for s in students:
            if s[1].lower() == search_name.lower():
                print(f"{s[0]}\t{s[1]}\t{s[2]}\t{s[3]}\t{s[4]}")
                found = True

        if not found:
            print("Student not found.")

    elif choice == '4':
        update_det = input("Enter field to update (name/age/course/marks): ").lower()
        update_id = input("Enter Student ID: ")

        for s in students:
            if s[0] == update_id:
                if update_det == 'name':
                    s[1] = input("Enter new name: ")
                elif update_det == 'age':
                    s[2] = int(input("Enter new age: "))
                elif update_det == 'course':
                    s[3] = input("Enter new course: ")
                elif update_det == 'marks':
                    s[4] = int(input("Enter new marks: "))
                else:
                    print("Invalid field.")
                    break
                print("Student details updated successfully!")
                break
        else:
            print("Invalid Student ID.")

    elif choice == '5':
        delete_id = input("Enter Student ID to delete: ")

        for s in students:
            if s[0] == delete_id:
                students.remove(s)
                print("Student deleted successfully!")
                break
        else:
            print("Invalid Student ID.")

    elif choice == '6':
        print("Saving data and exiting...")
        break
