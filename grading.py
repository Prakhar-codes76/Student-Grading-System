def calculate_average(grades):
    if not grades:
        return 0
    return sum(grades) / len(grades)

# Login System
login = input("Enter username: ")
password = int(input("Enter password: "))

if login == "admin" and password == 1234:
    print("Welcome to Grade Central")
    
    
    all_students = {}
    
    
    while True:
        print("\n--- Menu ---")
        print("1. Add a student")
        print("2. Remove a student")
        print("3. Show all students and averages")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            name = input("Enter student name: ")
            grades = []
            while True:
                g = input(f"Enter grade for {name} (or 'done'): ")
                if g.lower() == 'done': break
                try:
                    grades.append(float(g))
                except ValueError:
                    print("Please enter a valid number.")
            
            
            all_students[name] = calculate_average(grades)
            print(f"Student {name} added.")

        elif choice == '2':
            name = input("Enter name to remove: ")
            if name in all_students:
                del all_students[name]
                print(f"{name} removed.")
            else:
                print("Student not found.")

        elif choice == '3':
            print("\n--- Student Averages ---")
            for name, avg in all_students.items():
                print(f"Name: {name} | Average: {avg:.2f}")

        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")
else:
    print("Wrong username or password!") 