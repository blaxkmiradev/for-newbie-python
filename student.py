import json
import os

FILE = "students.json"

def load_data():
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            return json.load(f)
    return []

def save_data(data):
    with open(FILE, "w") as f:
        json.dump(data, f, indent=4)

students = load_data()

while True:
    print("\n=== School Manager ===")
    print("1. Add Students")
    print("2. View Students")
    print("3. Delete Students")
    print("4. Exit")

    choice = input("Choose: ")

    if choice == "1":
        name = input("Student name: ")
        age = input("Age: ")
        student = {"name": name, "age": age}
        students.append(student)
        save_data(students)
        print("Added!")

    elif choice == "2":
        if not students:
            print("No Students.")
        else:
            for i, s in enumerate(students):
                print(f"{i+1}. {s['name']} (Age: {s['age']})")

    elif choice == "3":
        index = int(input("Enter number to delete: ")) - 1

        if 0 <= index < len(students):
            removed = students.pop(index)
            save_data(students)
            print("Deleted:", removed["name"])
        else:
            print("Invalid number!")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice")