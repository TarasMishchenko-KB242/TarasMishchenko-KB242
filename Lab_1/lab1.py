# lab_01.py

# Початковий список студентів (вже відсортований)
students = [
    {"name": "Bob",  "phone": "0631111111", "email": "bob@gmail.com",  "group": "KB-22-1"},
    {"name": "Emma", "phone": "0632222222", "email": "emma@gmail.com", "group": "KB-22-1"},
    {"name": "Jon",  "phone": "0633333333", "email": "jon@gmail.com",  "group": "KB-22-2"},
    {"name": "Zak",  "phone": "0634444444", "email": "zak@gmail.com",  "group": "KB-22-2"}
]


# Виведення всього списку
def printAllList():
    print("\n--- Список студентів ---")
    for elem in students:
        strForPrint = (f"Ім'я: {elem['name']},  Телефон: {elem['phone']},  "
                       f"Email: {elem['email']},  Група: {elem['group']}")
        print(strForPrint)
    print("-------------------------\n")


# Додавання нового студента з урахуванням сортування
def addNewElement():
    name = input("Введіть ім'я студента: ")
    phone = input("Введіть телефон студента: ")
    email = input("Введіть email студента: ")
    group = input("Введіть групу студента: ")
    newItem = {"name": name, "phone": phone, "email": email, "group": group}

    # Знайти позицію для вставки (щоб зберегти сортування)
    insertPosition = 0
    for item in students:
        if name > item["name"]:
            insertPosition += 1
        else:
            break
    students.insert(insertPosition, newItem)
    print("сНового студента додано!\n")


# Видалення студента за ім’ям
def deleteElement():
    name = input("Введіть ім'я студента для видалення: ")
    deletePosition = -1
    for item in students:
        if name == item["name"]:
            deletePosition = students.index(item)
            break
    if deletePosition == -1:
        print("Студента не знайдено.\n")
    else:
        del students[deletePosition]
        print("Студента видалено!\n")


# Оновлення інформації про студента
def updateElement():
    name = input("Введіть ім'я студента, якого потрібно оновити: ")
    found = False
    for item in students:
        if item["name"] == name:
            found = True
            print(f"🔹 Поточні дані: {item}")
            new_name = input(f"Нове ім'я (або Enter, щоб залишити '{item['name']}'): ") or item["name"]
            new_phone = input(f"Новий телефон (або Enter, щоб залишити '{item['phone']}'): ") or item["phone"]
            new_email = input(f"Новий email (або Enter, щоб залишити '{item['email']}'): ") or item["email"]
            new_group = input(f"Нова група (або Enter, щоб залишити '{item['group']}'): ") or item["group"]

            # Видаляємо старий запис
            students.remove(item)
            # Додаємо оновлений запис (з урахуванням сортування)
            new_item = {"name": new_name, "phone": new_phone, "email": new_email, "group": new_group}

            insertPosition = 0
            for s in students:
                if new_name > s["name"]:
                    insertPosition += 1
                else:
                    break
            students.insert(insertPosition, new_item)
            print("Дані студента оновлено!\n")
            break

    if not found:
        print("Студента не знайдено.\n")


# Головне меню
def main():
    while True:
        choice = input("Оберіть дію [C - створити, U - оновити, D - видалити, P - показати, X - вихід]: ").strip().lower()
        match choice:
            case "c":
                print("Додавання нового студента:")
                addNewElement()
                printAllList()
            case "u":
                print("Оновлення даних студента:")
                updateElement()
                printAllList()
            case "d":
                print("Видалення студента:")
                deleteElement()
                printAllList()
            case "p":
                printAllList()
            case "x":
                print("Вихід з програми.")
                break
            case _:
                print("Невірний вибір, спробуйте ще раз.\n")


# Запуск головної функції
main()