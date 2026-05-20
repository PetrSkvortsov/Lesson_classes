class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecture(self, lecturer, course, lecturer_grades):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.lecture_grades:
                lecturer.lecture_grades[course] += [lecturer_grades]
            else:
                lecturer.lecture_grades[course] = [lecturer_grades]
        else:
            return 'Ошибка'
    def __str__(self):
        student_grades = []
        for gardes_list in self.grades.values():
            student_grades += gardes_list
        if student_grades:
            average = sum(student_grades) / len(student_grades)
        else:
            average = 0

        if self.courses_in_progress:
            student_courses = ', '.join(self.courses_in_progress)
        else:
            student_courses = 'Нет курсов в прогрессе'

        if self.finished_courses:
            finished_courses = ', '.join(self.finished_courses)
        else:
            finished_courses = 'Нет завершенных курсов'
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {average}\nКурсы в процессе изучения: {student_courses}\nЗавершенные курсы: {finished_courses}"

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.lecture_grades = {}

    def __str__(self):
        lecturer_grades = []
        for grades_list in self.lecture_grades.values():
            lecturer_grades += grades_list
        if lecturer_grades:
            average = sum(lecturer_grades) / len(lecturer_grades)
        else:
            average = 0
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {average}"

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"

# средняя оценка за домашние задания
def average_hw_grade(students, course):
    student_grades = []
    for student in students:
        if course in student.grades:
            student_grades += student.grades[course]
    if student_grades:
        return sum(student_grades) / len(student_grades)
    return 0

# средняя оценка за лекции
def average_lecture_grade(lecturers, course):
    lecturer_grades = []
    for lecturer in lecturers:
        if course in lecturer.lecture_grades:
            lecturer_grades += lecturer.lecture_grades[course]
    if lecturer_grades:
        return sum(lecturer_grades) / len(lecturer_grades)
    return 0

lecturer = Lecturer('Иван', 'Иванов')
reviewer = Reviewer('Пётр', 'Петров')
student = Student('Алёхина', 'Ольга', 'Ж')

# второй экзекмпляр людей
student2 = Student('Алейсей', 'Пчелкин', 'М')
lecturer2 = Lecturer('Сергей', 'Швецов')
reviewer2 = Reviewer('Анна', 'Сидорова')

student.courses_in_progress += ['Python', 'Java']
lecturer.courses_attached += ['Python', 'C++']
reviewer.courses_attached += ['Python', 'C++']

# второй экземпляр курсов
student2.courses_in_progress += ['Python', 'Java']
lecturer2.courses_attached += ['Python', 'C++']
reviewer2.courses_attached += ['Python', 'C++']

# выставлене оценок студентам
reviewer.rate_hw(student, 'Python', 8)
reviewer.rate_hw(student, 'Python', 9)
reviewer.rate_hw(student, 'Java', 7)
reviewer2.rate_hw(student2, 'Python', 10)
reviewer2.rate_hw(student2, 'Python', 6)

# выставление оценок  лекторам
student.rate_lecture(lecturer, 'Python', 10)
student.rate_lecture(lecturer, 'Python', 9)
student2.rate_lecture(lecturer, 'Python', 8)
student.rate_lecture(lecturer2, 'Java', 7)

print(average_hw_grade([student, student2], 'Python'))
print(average_lecture_grade([lecturer, lecturer2], 'Python'))