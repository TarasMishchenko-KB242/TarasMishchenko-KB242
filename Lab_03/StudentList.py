from Student import Student

class StudentList:
    def __init__(self):
        self.students = []

    def add_student(self, student: Student):
        """Додає студента та зберігає сортування за ім'ям."""
        insert_pos = 0
        for i, s in enumerate(self.students):
            if student.name > s.name:
                insert_pos = i + 1
            else:
                break
        self.students.insert(insert_pos, student)

    def delete_student(self, name):
        """Видаляє студента за ім'ям."""
        for s in self.students:
            if s.name == name:
                self.students.remove(s)
                return True
        return False

    def update_student(self, old_name, updated_student: Student):
        """Оновлює дані студента."""
        if self.delete_student(old_name):
            self.add_student(updated_student)
            return True
        return False

    def get_all(self):
        return self.students