import logging
import datetime

# ЗАВДАННЯ 1: Калькулятор з механізмом логування

# Налаштування логування
# Файл 'app_log.txt' буде створено в тій же папці, де лежить скрипт
logging.basicConfig(
    filename='app_log.txt',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    encoding='utf-8'
)

# Імітація модуля functions.py
def add(a, b): return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b
def divide(a, b):
    if b == 0:
        return "Помилка: ділення на нуль"
    return a / b

# Імітація модуля operations.py з додаванням логування
def get_input(prompt):
    while True:
        user_input = input(prompt)
        try:
            value = float(user_input)
            # Логуємо введені дані
            logging.info(f"Введення даних: користувач ввів число {value}")
            return value
        except ValueError:
            logging.error(f"Помилка введення: користувач намагався ввести '{user_input}'")
            print("Помилка! Будь ласка, введіть число.")

def run_calculator():
    print("\n--- Калькулятор з логуванням (Завдання 1) ---")
    print("Всі дії записуються у файл 'app_log.txt'")
    
    num1 = get_input("Введіть перше число: ")
    operation = input("Оберіть операцію (+, -, *, /): ").strip()
    num2 = get_input("Введіть друге число: ")

    result = None
    if operation == '+': result = add(num1, num2)
    elif operation == '-': result = subtract(num1, num2)
    elif operation == '*': result = multiply(num1, num2)
    elif operation == '/': result = divide(num1, num2)
    else:
        result = "Невідома операція"
        logging.warning(f"Спроба виконати невідому операцію: '{operation}'")

    # Фінальне логування результату
    log_message = f"ВИКОНАНО: {num1} {operation} {num2} | РЕЗУЛЬТАТ: {result}"
    logging.info(log_message)
    
    print(f"Результат: {result}")


# ЗАВДАННЯ 2: Сортування списку словників (Lambda)

def run_sorting():
    print("\n--- Сортування словників (Завдання 2) ---")
    
    # Несортований список словників
    data = [
        {"name": "Олександр", "grade": 95},
        {"name": "Марія", "grade": 82},
        {"name": "Андрій", "grade": 100},
        {"name": "Тетяна", "grade": 74},
        {"name": "Борис", "grade": 88}
    ]

    print("Початковий список:")
    for item in data: print(f"  {item}")

    # Сортування за ім'ям (lambda повертає значення за ключем 'name')
    sorted_by_name = sorted(data, key=lambda x: x['name'])
    
    # Сортування за оцінкою (lambda повертає значення за ключем 'grade')
    sorted_by_grade = sorted(data, key=lambda x: x['grade'], reverse=True)

    print("\nВідсортовано за ІМ'ЯМ:")
    for item in sorted_by_name: print(f"  {item}")

    print("\nВідсортовано за ОЦІНКОЮ (від найвищої):")
    for item in sorted_by_grade: print(f"  {item}")


# ГОЛОВНИЙ ЦИКЛ ПРОГРАМИ

def main():
    while True:
        print("\nГоловне меню:")
        print("1. Запустити калькулятор (з логуванням)")
        print("2. Показати роботу сортування (lambda)")
        print("0. Вихід")
        
        choice = input("Ваш вибір: ")
        
        if choice == '1':
            run_calculator()
        elif choice == '2':
            run_sorting()
        elif choice == '0':
            print("Вихід з програми...")
            break
        else:
            print("Невірний вибір!")

if __name__ == "__main__":
    main()