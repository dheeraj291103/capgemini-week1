def calculate_grade(percentage):
    if percentage >= 90:
        return 'A'
    elif percentage >= 80:
        return 'B'
    elif percentage >= 70:
        return 'C'
    elif percentage >= 60:
        return 'D'
    else:
        return 'F'
def main():
    student_name = input("Enter student name: ")      
    subjects = ['Maths', 'English', 'Telugu', 'Science', 'Social Studies']
    marks = []
    for subject in subjects:
        marks.append(int(input(f"Enter marks for {subject}: ")))
        total_marks = sum(marks)
        percentage=(total_marks/500)*100
        grade=calculate_grade(total_marks)
    
        print(f'Total marks obtained by {student_name} is {total_marks}')
        print(f'Percentage obtained by {student_name} is {percentage}')
        print(f'Grade obtained by {student_name} is {grade}')
if __name__ == "__main__":
    main()


