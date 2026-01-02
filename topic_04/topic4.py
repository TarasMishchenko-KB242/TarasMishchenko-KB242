# --- ЗАВДАННЯ 1: Функція запиту даних з обробкою виняткових ситуацій ---
def get_number(prompt):
    while True:
        try:
            # Намагаємось перетворити введення на число з плаваючою крапкою
            return float(input(prompt))
        except ValueError:
            # Обробка помилки, якщо користувач ввів текст замість числа
            print("Помилка: Ви ввели не число. Спробуйте ще раз.")

# Базові функції операцій
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

# --- ЗАВДАННЯ 2: Функція ділення з обробкою ділення на нуль ---
def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        # Обробка помилки ділення на нуль
        return "Помилка: Ділення на нуль неможливе!"

# Головна функція калькулятора (Метод нескінченного введення)
def calculator():
    print("Вітаємо у калькуляторі!")
    
    while True:
        print("\n--- Нове обчислення ---")
        
        # Використовуємо функцію із Завдання 1
        num1 = get_number("Введіть перше число: ")
        
        operation = input("Оберіть операцію (+, -, *, /) або 'q' для виходу: ")
        
        if operation.lower() == 'q':
            print("Вихід з програми...")
            break
            
        if operation not in ['+', '-', '*', '/']:
            print("Помилка: Невідома операція!")
            continue

        num2 = get_number("Введіть друге число: ")

        # Виконання обчислень
        if operation == '+':
            print(f"Результат: {add(num1, num2)}")
        elif operation == '-':
            print(f"Результат: {subtract(num1, num2)}")
        elif operation == '*':
            print(f"Результат: {multiply(num1, num2)}")
        elif operation == '/':
            # Використовуємо функцію із Завдання 2
            result = divide(num1, num2)
            print(f"Результат: {result}")

if __name__ == "__main__":
    calculator()