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
        return_list = []
        for key, value in self.students.items():
            if value == grade_number:
                return_list.append(key)
        return sorted(return_list)

    def added(self):
        return self.addition_attempts
