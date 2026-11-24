
def calculate_grade(average):
    if average >= 90:
        return "S"
    elif average >= 80:
        return "A"
    elif average >= 65:
        return "B"
    elif average >= 50:
        return "C"
    elif average >= 40:
        return "D"
    else:
        return "F"


def main():
    print("===== STUDENT GRADE MANAGEMENT SYSTEM =====")

    name = input("Enter Student Name: ")
    department = input("Enter Department: ")
    semester = int(input("Enter Semester: "))

    marks = []

    for i in range(1, 4):
        while True:
            try:
                mark = float(input(f"Enter marks in Subject {i}: "))
                if 0 <= mark <= 100:
                    marks.append(mark)
                    break
                else:
                    print("Marks must be between 0 and 100.")
            except ValueError:
                print("Please enter a valid number.")

    average = sum(marks) / 3
    grade = calculate_grade(average)

    print("\n========== STUDENT RESULT ==========")
    print("Student Name:", name)
    print("Department:", department)
    print("Semester:", semester)
    print("Subject Marks:", marks)
    print("Average:", round(average, 2))
    print("Grade:", grade)
    print("===================================")


if __name__ == "__main__":
    main()
