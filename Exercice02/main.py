students = {
    "Alice": {"Mathematiques": 90, "Francais": 80, "Histoire": 95},
    "Bob": {"Mathematiques": 75, "Francais": 85, "Histoire": 70},
    "Charlie": {"Mathematiques": 88, "Francais": 92, "Histoire": 78},
}


def request_student_name():
    name = input("Entrez le nom de l'étudiant : ")
    return name


def display_student_grades(student_name: str, students: dict):
    student_name_lower = student_name.lower()
    for name, grades in students.items():
        if name.lower() == student_name_lower:
            print()
            print(f"Notes de {name} : ")
            print(f"Mathématiques : {grades['Mathematiques']}")
            print(f"Francais : {grades['Francais']}")
            print(f"Histoire : {grades['Histoire']}")
            return
    print(f"L'étudiant {student_name} n'existe pas dans la liste.")


def display_student_average(student_name: str, students: dict):
    student_name_lower = student_name.lower()
    total = 0
    for name, grades in students.items():
        if name.lower() == student_name_lower:
            for subject, grade in grades.items():
                total += grade
    average = total / len(students)
    print(f"Moyenne de {student_name} : {average:.2f}")


student_name = request_student_name()
student_notes = display_student_grades(student_name=student_name, students=students)
student_average = display_student_average(student_name=student_name, students=students)
