
    print("Welcome to Grade Central")
else:
    print("wrong username or password")
    Name = input("Enter the name of the Student:")
    Grades = input("Enter the grades of the Student:")
    average = sum(map(int, Grades.split())) / len(Grades.split())

subject = int(input("Enter the number of subject: "))