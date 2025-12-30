import math

# ЗАВДАННЯ 1: Пошук коренів квадратного рівняння

def calc_discriminant(a, b, c):
    """Функція розрахунку дискримінанту з попередньої теми"""
    return b**2 - 4*a*c

def solve_quadratic(a, b, c):
    """Функція пошуку коренів через умовні переходи"""
    if a == 0:
        return "Помилка: 'a' не може дорівнювати 0 (це не квадратне рівняння)."
    
    d = calc_discriminant(a, b, c)
    print(f"Аналіз рівняння {a}x^2 + ({b})x + ({c}) = 0")
    print(f"Дискримінант D = {d}")

    if d > 0:
        x1 = (-b + math.sqrt(d)) / (2 * a)
        x2 = (-b - math.sqrt(d)) / (2 * a)
        return f"Два корені: x1 = {x1}, x2 = {x2}"
    elif d == 0:
        x = -b / (2 * a)
        return f"Один корінь: x = {x}"
    else:
        return "Коренів немає (D < 0)"

print("--- ЗАВДАННЯ 1: Квадратне рівняння ---")
# Приклад: x^2 - 5x + 6 = 0
print(solve_quadratic(1, -5, 6))
print("-" * 40 + "\n")


# ФУНКЦІЇ ДЛЯ КАЛЬКУЛЯТОРА (Завдання 2 та 3)

def add(x, y): return x + y
def subtract(x, y): return x - y
def multiply(x, y): return x * y
def divide(x, y):
    if y == 0:
        return "Помилка: ділення на нуль!"
    return x / y

# ЗАВДАННЯ 2: Калькулятор (if-else)

print("--- ЗАВДАННЯ 2: Калькулятор (if-else) ---")
try:
    num1 = float(input("Введіть перше число: "))
    num2 = float(input("Введіть друге число: "))
    operation = input("Оберіть операцію (+, -, *, /): ")

    if operation == '+':
        result = add(num1, num2)
    elif operation == '-':
        result = subtract(num1, num2)
    elif operation == '*':
        result = multiply(num1, num2)
    elif operation == '/':
        result = divide(num1, num2)
    else:
        result = "Невідома операція!"
    
    print(f"Результат (if-else): {result}")
except ValueError:
    print("Помилка: введено не число!")

print("-" * 40 + "\n")


# ЗАВДАННЯ 3: Калькулятор (match-case)

print("--- ЗАВДАННЯ 3: Калькулятор (match-case) ---")
try:
    n1 = float(input("Введіть перше число: "))
    n2 = float(input("Введіть друге число: "))
    op = input("Оберіть операцію (+, -, *, /): ")

    match op:
        case '+':
            res = add(n1, n2)
        case '-':
            res = subtract(n1, n2)
        case '*':
            res = multiply(n1, n2)
        case '/':
            res = divide(n1, n2)
        case _:
            res = "Невідома операція!"

    print(f"Результат (match): {res}")
except ValueError:
    print("Помилка: введено не число!")

print("-" * 40)