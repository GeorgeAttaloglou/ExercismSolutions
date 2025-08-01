class School:

    def __init__(self):
        self.students = {}
        self.addition_attempts = []

    def add_student(self, name, grade):
        if name not in self.students.keys():
            self.students[name] = grade
            self.addition_attempts.append(True)
        else:
            self.addition_attempts.append(False)

    def roster(self) -> list:
        sorted_students = sorted(self.students.items(), key=lambda x: (x[1], x[0]))
        return [name for name, grade in sorted_students]

    def grade(self, grade_number) -> list:
        return sorted(name for name, grade in self.students.items() if grade == grade_number)

    def added(self):
        return self.addition_attempts
