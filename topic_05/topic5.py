import random
import requests

# ЗАВДАННЯ 1: Камінь, ножиці, папір

def task_1_game():
    print("\n--- ГРА: Камінь, ножиці, папір ---")
    choices = ["stone", "scissor", "paper"]
    
    user_choice = input("Ваш вибір (stone, scissor, paper): ").lower().strip()
    if user_choice not in choices:
        print("Помилка! Невірний вибір.")
        return

    computer_choice = random.choice(choices)
    print(f"Комп'ютер обрав: {computer_choice}")

    if user_choice == computer_choice:
        print("Результат: Нічия!")
    elif (user_choice == "stone" and computer_choice == "scissor") or \
         (user_choice == "scissor" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "stone"):
        print("Результат: Ви перемогли!")
    else:
        print("Результат: Ви програли!")


# ЗАВДАННЯ 2: Конвертер валют (API НБУ)

def task_2_converter():
    print("\n--- КОНВЕРТЕР ВАЛЮТ (НБУ) ---")
    currency = input("Введіть валюту (USD, EUR, PLN): ").upper().strip()
    try:
        amount = float(input(f"Введіть кількість {currency}: "))
    except ValueError:
        print("Помилка: введіть число.")
        return

    print("Отримання курсу з банку...")
    try:
        # Запит до API Національного Банку України
        response = requests.get("https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json")
        data = response.json()
        
        rate = next((item['rate'] for item in data if item['cc'] == currency), None)
        
        if rate:
            result = amount * rate
            print(f"Курс {currency}: {rate:.2f}")
            print(f"Результат: {amount} {currency} = {result:.2f} UAH")
        else:
            print("Валюту не знайдено.")
    except Exception as e:
        print(f"Помилка зв'язку з сервером: {e}")


# ЗАВДАННЯ 3: Калькулятор (Логіка модулів в одному місці)

# Імітація functions.py (Математика)
def add(a, b): return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b
def divide(a, b):
    return a / b if b != 0 else "Помилка: ділення на нуль"

# Імітація operations.py (Введення та логіка)
def get_num(msg):
    while True:
        try: return float(input(msg))
        except ValueError: print("Це не число!")

def task_3_calculator():
    print("\n--- МОДУЛЬНИЙ КАЛЬКУЛЯТОР ---")
    n1 = get_num("Перше число: ")
    op = input("Операція (+, -, *, /): ")
    n2 = get_num("Друге число: ")

    if op == '+': print("Разом:", add(n1, n2))
    elif op == '-': print("Різниця:", subtract(n1, n2))
    elif op == '*': print("Добуток:", multiply(n1, n2))
    elif op == '/': print("Частка:", divide(n1, n2))
    else: print("Невідома операція.")


# ГОЛОВНЕ МЕНЮ

def main():
    while True:
        print("\n==============================")
        print("ОБЕРІТЬ ЗАВДАННЯ:")
        print("1 - Гра 'Камінь, ножиці, папір'")
        print("2 - Конвертер валют (API НБУ)")
        print("3 - Калькулятор (Завдання 3)")
        print("0 - Вихід")
        
        choice = input("\nВаш вибір: ")
        
        if choice == '1':
            task_1_game()
        elif choice == '2':
            task_2_converter()
        elif choice == '3':
            task_3_calculator()
        elif choice == '0':
            print("Завершення роботи.")
            break
        else:
            print("Невірний вибір, спробуйте ще раз.")

if __name__ == "__main__":
    main()