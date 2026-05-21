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
        # вычисение средней оценки
        student_grades = []
        for gardes_list in self.grades.values():
            student_grades += gardes_list
        if student_grades:
            average = sum(student_grades) / len(student_grades)
        else:
            average = 0
#       список всех курсов в in_progress
        if self.courses_in_progress:
            student_courses = ', '.join(self.courses_in_progress)
        else:
            student_courses = 'Нет курсов в прогрессе'
#       список всех пройденных курсов
        if self.finished_courses:
            finished_courses = ', '.join(self.finished_courses)
        else:
            finished_courses = 'Нет завершенных курсов'
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {average}\nКурсы в процессе изучения: {student_courses}\nЗавершенные курсы: {finished_courses}"

    # метод для сравнения студентов скрываем _average_grade чтобы вызов сравнения был только через знаки сравнения
    def _average_grade(self):
        student_grades = []
        for grades_list in self.grades.values():
            student_grades += grades_list
        if student_grades:
            return sum(student_grades) / len(student_grades)
        return 0

    def __gt__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self._average_grade() > other._average_grade()

    def __lt__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self._average_grade() < other._average_grade()

    def __eq__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self._average_grade() == other._average_grade()

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.lecture_grades = {}

        #     применение магического метода
    def __str__(self):
        lecturer_grades = []
        for grades_list in self.lecture_grades.values():
            lecturer_grades += grades_list
        if lecturer_grades:
            average = sum(lecturer_grades) / len(lecturer_grades)
        else:
             average = 0
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {average}"

    # методы для сравнения лекторов
    def _average_grade(self):
        lecturer_grades = []
        for grades_list in self.lecture_grades.values():
            lecturer_grades += grades_list
        if lecturer_grades:
            return sum(lecturer_grades) / len(lecturer_grades)
        return 0

    def __gt__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self._average_grade() > other._average_grade()

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self._average_grade() < other._average_grade()

    def __eq__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self._average_grade() == other._average_grade()

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

lecturer = Lecturer('Иван', 'Иванов')
reviewer = Reviewer('Пётр', 'Петров')
student = Student('Алёхина', 'Ольга', 'Ж')

student.courses_in_progress += ['Python', 'Java']
lecturer.courses_attached += ['Python', 'C++']
reviewer.courses_attached += ['Python', 'C++']

print(f"{reviewer}\n")
print(f"{lecturer}\n")
print(f"{student}")
