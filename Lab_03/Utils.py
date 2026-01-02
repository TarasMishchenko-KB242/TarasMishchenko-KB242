import csv
from Student import Student

class FileUtils:
    @staticmethod
    def load_from_csv(file_name):
        students_objs = []
        try:
            with open(file_name, mode='r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    students_objs.append(Student(row['name'], row['phone'], row['email'], row['group']))
        except FileNotFoundError:
            print(f"Файл {file_name} не знайдено.")
        return students_objs

    @staticmethod
    def save_to_csv(file_name, student_list):
        fieldnames = ["name", "phone", "email", "group"]
        with open(file_name, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for s in student_list:
                writer.writerow(s.to_dict())