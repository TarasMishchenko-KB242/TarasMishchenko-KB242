import sys
from Student import Student
from StudentList import StudentList
from Utils import FileUtils

def main():
    if len(sys.argv) < 2:
        print("Використання: python main.py <назва_файлу.csv>")
        return

    file_name = sys.argv[1]
    group_list = StudentList()
    
    # Завантаження початкових даних
    initial_data = FileUtils.load_from_csv(file_name)
    for s in initial_data:
        group_list.add_student(s)

    while True:
        choice = input("\n[C]reate, [U]pdate, [D]elete, [P]rint, [X]it: ").strip().lower()

        if choice == 'c':
            name = input("Ім'я: ")
            phone = input("Телефон: ")
            email = input("Email: ")
            group = input("Група: ")
            group_list.add_student(Student(name, phone, email, group))
        
        elif choice == 'u':
            name = input("Якого студента оновити? ")
            new_name = input("Нове ім'я: ")
            new_phone = input("Новий телефон: ")
            new_email = input("Новий email: ")
            new_group = input("Нова група: ")
            if group_list.update_student(name, Student(new_name, new_phone, new_email, new_group)):
                print("Оновлено.")
            else:
                print("Не знайдено.")

        elif choice == 'd':
            name = input("Ім'я для видалення: ")
            if group_list.delete_student(name):
                print("Видалено.")
            else:
                print("Не знайдено.")

        elif choice == 'p':
            for s in group_list.get_all():
                print(s)

        elif choice == 'x':
            FileUtils.save_to_csv(file_name, group_list.get_all())
            print("Дані збережено. Бувай!")
            break

if __name__ == "__main__":
    main()