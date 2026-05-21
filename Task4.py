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
            if course in lecturer.grades:
                lecturer.grades[course] += [lecturer_grades]
            else:
                lecturer.grades[course] = [lecturer_grades]
            return f"поставил {lecturer_grades} за курс {course}"
        else:
            return 'Ошибка'
    def __str__(self):
        student_grades = []
        for grades_list in self.grades.values():
            student_grades += grades_list
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
        self.grades = {}

    def __str__(self):
        lecturer_grades = []
        for grades_list in self.grades.values():
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
            return f"поставил {grade} по {course}"
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
        if course in lecturer.grades:
            lecturer_grades += lecturer.grades[course]
    if lecturer_grades:
        return sum(lecturer_grades) / len(lecturer_grades)
    return 0

lecturer = Lecturer('Иван', 'Иванов')
reviewer = Reviewer('Пётр', 'Петров')
student = Student('Алёхина', 'Ольга', 'Ж')

# второй экзекмпляр людей
student2 = Student('Алексей', 'Пчелкин', 'М')
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

# дополнительная демонстрация
new_student = Student('Смирнова', 'Екатерина', 'Ж')
new_lecturer = Lecturer('Соколов', 'Дмитрий')
new_reviewer = Reviewer('Михайлова', 'Ольга')

new_student.courses_in_progress += ['Python', 'Git']
new_lecturer.courses_attached += ['Python', 'Java']
new_reviewer.courses_attached += ['Python', 'Git']

print("\n1. Назначенные курсы:")
print(f"Студент {new_student.name} {new_student.surname} изучает курсы: {new_student.courses_in_progress}")
print(f"Лектор {new_lecturer.name} {new_lecturer.surname} ведет курсы: {new_lecturer.courses_attached}")
print(f"Проверяющий {new_reviewer.name} {new_reviewer.surname} проверяет курсы: {new_reviewer.courses_attached}\n")

print("\n2. Выставление оценок:")
result1 = new_reviewer.rate_hw(new_student, 'Python', 9)
print(f"Проверяющий {new_reviewer.name} {new_reviewer.surname} оценил(а) {new_student.name} {new_student.surname} по Python: {result1}")

result2 = new_student.rate_lecture(new_lecturer, 'Python', 8)
print(f"Студент {new_student.name} {new_student.surname} оценил(а) {new_lecturer.name} {new_lecturer.surname} по Python: {result2}")

print("\n3. Негативные сценарии выставления ошибок:")
result3 = new_reviewer.rate_hw(new_student, 'Java', 8)
print(f"Проверяющий {new_reviewer.name} {new_reviewer.surname} пробует оценить студента по Java (студент не изучает курс): {result3}")

result4 = new_reviewer.rate_hw(new_lecturer, 'Python', 7)
print(f"Проверяющий {new_reviewer.name} {new_reviewer.surname} пробует оценить лектора: {result4}")

result5 = new_student.rate_lecture(new_lecturer, 'Java', 7)
print(f"Студент {new_student.name} {new_student.surname} пробует оценить лектора по Java (студент не изучает курс): {result5}")

result6 = new_student.rate_lecture(new_reviewer, 'Python', 9)
print(f"Студент {new_student.name} {new_student.surname} пробует оценить проверяющего: {result6}")

result7 = new_student.rate_lecture(new_lecturer, 'Git', 8)
print(f"Стуедент {new_student.name} {new_student.surname} пробует оценить по Git (лектор не ведет): {result7}")

print("\n4. Оцененные люди:")
print(f"Оценки студента {new_student.name}: {new_student.grades}")
print(f"Оценки лектора {new_lecturer.name}: {new_lecturer.grades}")