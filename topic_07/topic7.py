# ЗАВДАННЯ 2: Приклад використання __init__ та __str__

"""
__init__(self) — конструктор класу, викликається автоматично при створенні об'єкта.
__str__(self) — повертає рядкове представлення об'єкта (викликається функцією print()).
"""

class Book:
    def __init__(self, title, author):
        # Ініціалізація атрибутів
        self.title = title
        self.author = author

    def __str__(self):
        # Форматований вивід інформації про об'єкт
        return f"Книга: '{self.title}', автор: {self.author}"

# Приклад:
# my_book = Book("Кобзар", "Т. Шевченко")
# print(my_book) -> Виведе: Книга: 'Кобзар', автор: Т. Шевченко


# ЗАВДАННЯ 3: Клас Student та сортування через lambda

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Студент: {self.name.ljust(10)} | Вік: {self.age}"

def run_student_task():
    print("\n--- Завдання 3: Сортування списку об'єктів Student ---")
    
    # Створюємо список об'єктів
    students = [
        Student("Олексій", 20),
        Student("Марія", 18),
        Student("Анна", 21),
        Student("Дмитро", 19)
    ]

    # Сортування за віком (age) за допомогою lambda
    sorted_students = sorted(students, key=lambda s: s.age)

    print("Відсортовано за віком:")
    for student in sorted_students:
        print(student)


# ЗАВДАННЯ 4: ООП Калькулятор (Модульна структура в одному коді)

# Клас математичної логіки (відповідає за обчислення)
class MathEngine:
    def add(self, a, b): return a + b
    def subtract(self, a, b): return a - b
    def multiply(self, a, b): return a * b
    def divide(self, a, b):
        if b == 0:
            raise ZeroDivisionError("Ділення на нуль неможливе!")
        return a / b

# Клас інтерфейсу (відповідає за введення/виведення)
class UserInterface:
    @staticmethod
    def get_number(prompt):
        while True:
            try:
                return float(input(prompt))
            except ValueError:
                print("Помилка: введіть числове значення.")

    @staticmethod
    def get_operation():
        allowed = ['+', '-', '*', '/']
        while True:
            op = input(f"Оберіть дію ({', '.join(allowed)}) або 'q' для виходу: ").strip()
            if op in allowed or op.lower() == 'q':
                return op.lower()
            print("Невідома операція!")

# Головний клас-контролер (керує процесом)
class CalculatorApp:
    def __init__(self):
        # Інкапсулюємо об'єкти логіки та інтерфейсу
        self.engine = MathEngine()
        self.ui = UserInterface()

    def start(self):
        print("\n--- Завдання 4: ООП Калькулятор ---")
        while True:
            op = self.ui.get_operation()
            
            if op == 'q':
                print("Вихід з калькулятора.")
                break

            n1 = self.ui.get_number("Введіть перше число: ")
            n2 = self.ui.get_number("Введіть друге число: ")

            try:
                if op == '+': result = self.engine.add(n1, n2)
                elif op == '-': result = self.engine.subtract(n1, n2)
                elif op == '*': result = self.engine.multiply(n1, n2)
                elif op == '/': result = self.engine.divide(n1, n2)
                
                print(f"Результат: {result}")
            except ZeroDivisionError as e:
                print(f"Критична помилка: {e}")


# ГОЛОВНИЙ ЗАПУСК

if __name__ == "__main__":
    # 1. Демонстрація завдання зі студентами
    run_student_task()
    
    # 2. Демонстрація завдання з ООП калькулятором
    app = CalculatorApp()
    app.start()