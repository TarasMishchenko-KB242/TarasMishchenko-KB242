import math

# ДОПОМІЖНІ ФУНКЦІЇ З МИНУЛОЇ ТЕМИ
def add(x, y): return x + y
def subtract(x, y): return x - y
def multiply(x, y): return x * y
def divide(x, y):
    if y == 0: return "Помилка: ділення на нуль!"
    return x / y

# ЗАВДАННЯ 1: Калькулятор у циклі (Infinite Loop)

def task1_calculator():
    print("\n--- ЗАВДАННЯ 1: Калькулятор (введіть 'q' для виходу) ---")
    while True:
        choice = input("Натисніть Enter, щоб рахувати, або 'q' для виходу: ").lower()
        if choice == 'q':
            print("Робота калькулятора завершена.")
            break
        
        try:
            n1 = float(input("Введіть перше число: "))
            op = input("Оберіть операцію (+, -, *, /): ")
            n2 = float(input("Введіть друге число: "))

            match op:
                case '+': print(f"Результат: {add(n1, n2)}")
                case '-': print(f"Результат: {subtract(n1, n2)}")
                case '*': print(f"Результат: {multiply(n1, n2)}")
                case '/': print(f"Результат: {divide(n1, n2)}")
                case _: print("Невідома операція!")
        except ValueError:
            print("Помилка: введіть коректні числа!")
        print("-" * 20)

# ЗАВДАННЯ 2: Тестування функцій списків

def task2_lists():
    print("\n--- ЗАВДАННЯ 2: Тестування списків ---")
    lst = [10, 20, 30]
    print(f"Початковий список: {lst}")
    
    lst.append(40)          # Додає в кінець
    print(f"append(40): {lst}")
    
    lst.extend([50, 60])    # Розширює іншим списком
    print(f"extend([50, 60]): {lst}")
    
    lst.insert(1, 15)       # Вставка на позицію id=1 значення val=15
    print(f"insert(1, 15): {lst}")
    
    lst.remove(20)          # Видаляє перше входження значення 20
    print(f"remove(20): {lst}")
    
    lst_copy = lst.copy()   # Копіювання
    print(f"copy(): Створено копію {lst_copy}")
    
    lst.reverse()           # Розвертає список
    print(f"reverse(): {lst}")
    
    lst.sort()              # Сортує
    print(f"sort(): {lst}")
    
    lst.clear()             # Очищує список
    print(f"clear(): {lst}")


# ЗАВДАННЯ 3: Тестування функцій словників

def task3_dicts():
    print("\n--- ЗАВДАННЯ 3: Тестування словників ---")
    user = {"name": "Ivan", "age": 25}
    print(f"Початковий словник: {user}")
    
    user.update({"city": "Kyiv", "age": 26}) # Оновлення/додавання
    print(f"update(): {user}")
    
    print(f"keys(): {list(user.keys())}")     # Тільки ключі
    print(f"values(): {list(user.values())}") # Тільки значення
    print(f"items(): {list(user.items())}")   # Пари (ключ, значення)
    
    del user["name"]                          # Видалення за ключем
    print(f"del user['name']: {user}")
    
    user.clear()                              # Очищення
    print(f"clear(): {user}")

# ЗАВДАННЯ 4: Пошук позиції для вставки у відсортований список

def find_insert_position(sorted_list, new_element):
    """Шукає індекс, куди вставити елемент, щоб список лишився відсортованим"""
    for i in range(len(sorted_list)):
        if sorted_list[i] >= new_element:
            return i
    return len(sorted_list) # Якщо елемент найбільший, вставляємо в кінець

def task4_insertion():
    print("\n--- ЗАВДАННЯ 4: Пошук позиції для вставки ---")
    my_sorted_list = [10, 20, 30, 40, 50]
    element = 35
    
    pos = find_insert_position(my_sorted_list, element)
    print(f"Список: {my_sorted_list}")
    print(f"Куди вставити число {element}? Відповідь: індекс {pos}")
    
    # Перевірка вставкою
    my_sorted_list.insert(pos, element)
    print(f"Список після вставки: {my_sorted_list}")

# ЗАПУСК УСІХ ЗАВДАНЬ

if __name__ == "__main__":
    # Завдання 2, 3, 4 запускаються автоматично для демонстрації
    task2_lists()
    task3_dicts()
    task4_insertion()
    
    # Калькулятор запускаємо останнім, бо він має нескінченний цикл
    task1_calculator()