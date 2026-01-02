import csv
import sys

# Глобальний список студентів
students = []

def load_data(file_name):
    """Завантажує дані з CSV файлу."""
    global students
    try:
        with open(file_name, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            students = []
            for row in reader:
                students.append(row)
            # Сортуємо список після завантаження про всяк випадок
            students.sort(key=lambda x: x['name'])
        print(f"Дані успішно завантажені з файлу: {file_name}")
    except FileNotFoundError:
        print(f"Файл {file_name} не знайдено. Починаємо з порожнім списком.")
    except Exception as e:
        print(f"Помилка при завантаженні: {e}")

def save_data(file_name):
    """Зберігає дані у CSV файл."""
    fieldnames = ["name", "phone", "email", "group"]
    try:
        with open(file_name, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(students)
        print(f"Дані успішно збережені у файл: {file_name}")
    except Exception as e:
        print(f"Помилка при збереженні: {e}")

def printAllList():
    print("\n--- Список студентів ---")
    for elem in students:
        strForPrint = (f"Ім'я: {elem['name']}, Телефон: {elem['phone']}, "
                       f"Email: {elem['email']}, Група: {elem['group']}")
        print(strForPrint)
    print("-------------------------\n")

def addNewElement(name, phone, email, group):
    """Додає нового студента (функція винесена для зручності тестування)."""
    newItem = {"name": name, "phone": phone, "email": email, "group": group}
    insertPosition = 0
    for item in students:
        if name > item["name"]:
            insertPosition += 1
        else:
            break
    students.insert(insertPosition, newItem)
    return True

def deleteElement(name):
    """Видаляє студента за ім'ям."""
    for item in students:
        if item["name"] == name:
            students.remove(item)
            return True
    return False

def updateElement(name, new_name, new_phone, new_email, new_group):
    """Оновлює дані студента."""
    if deleteElement(name):
        addNewElement(new_name, new_phone, new_email, new_group)
        return True
    return False

def main():
    # Перевірка наявності аргументу командного рядка (ім'я файлу)
    if len(sys.argv) < 2:
        print("Помилка: Не вказано ім'я файлу для завантаження!")
        print("Запуск: python lab2.py data.csv")
        return

    file_name = sys.argv[1]
    load_data(file_name)

    while True:
        choice = input("Оберіть дію [C - створити, U - оновити, D - видалити, P - показати, X - вихід]: ").strip().lower()
        
        match choice:
            case "c":
                name = input("Введіть ім'я: ")
                phone = input("Введіть телефон: ")
                email = input("Введіть email: ")
                group = input("Введіть групу: ")
                addNewElement(name, phone, email, group)
                print("Студента додано!")
                printAllList()
            case "u":
                name = input("Ім'я студента для оновлення: ")
                # Знаходимо поточні дані для зручності
                current = next((s for s in students if s['name'] == name), None)
                if current:
                    n_name = input(f"Нове ім'я ({current['name']}): ") or current['name']
                    n_phone = input(f"Новий телефон ({current['phone']}): ") or current['phone']
                    n_email = input(f"Новий email ({current['email']}): ") or current['email']
                    n_group = input(f"Нова група ({current['group']}): ") or current['group']
                    updateElement(name, n_name, n_phone, n_email, n_group)
                    print("Дані оновлено!")
                else:
                    print("Студента не знайдено.")
                printAllList()
            case "d":
                name = input("Ім'я для видалення: ")
                if deleteElement(name):
                    print("Студента видалено.")
                else:
                    print("Студента не знайдено.")
                printAllList()
            case "p":
                printAllList()
            case "x":
                save_data(file_name) # Збереження перед виходом
                print("Вихід з програми.")
                break
            case _:
                print("Невірний вибір.")

if __name__ == "__main__":
    main()