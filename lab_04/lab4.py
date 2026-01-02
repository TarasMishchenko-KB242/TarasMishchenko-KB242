import re

def get_tokens(expression):
    """Розбиває рядок на числа, оператори та дужки."""
    # Регулярний вираз для пошуку чисел (у тому числі з крапкою) та символів операторів
    return re.findall(r'\d+\.?\d*|[+\-*/^()]', expression)

def infix_to_rpn(tokens):
    """Перетворює інфіксний запис у ЗПЗ (алгоритм 'Сортувальна станція')."""
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    output = []
    stack = []

    for token in tokens:
        if re.match(r'\d+', token):  # Якщо число
            output.append(token)
        elif token == '(':           # Якщо відкриваюча дужка
            stack.append(token)
        elif token == ')':           # Якщо закриваюча дужка
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()              # Видаляємо '(' зі стека
        else:                        # Якщо оператор
            while (stack and stack[-1] != '(' and 
                   precedence.get(stack[-1], 0) >= precedence.get(token, 0)):
                output.append(stack.pop())
            stack.append(token)
    
    while stack:
        output.append(stack.pop())
        
    return output

def calculate_rpn(rpn_tokens):
    """Обчислює результат виразу, записаного в ЗПЗ."""
    stack = []
    
    for token in rpn_tokens:
        if re.match(r'\d+', token):
            stack.append(float(token))
        else:
            # Виштовхуємо два останніх операнди
            b = stack.pop()
            a = stack.pop()
            
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            elif token == '/':
                stack.append(a / b)
            elif token == '^':
                stack.append(a ** b)
                
    return stack[0]

# --- Основна частина програми ---

if __name__ == "__main__":
    print("Лабораторна робота №4: ЗПЗ та обчислення виразу")
    
    # Приклад виразу з завдання: 3 + 4 * 2 / (1 - 5) ^ 2
    input_expression = input("Введіть математичний вираз: ")
    
    try:
        # 1. Отримуємо токени
        tokens = get_tokens(input_expression)
        
        # 2. Перетворюємо в ЗПЗ
        rpn = infix_to_rpn(tokens)
        print(f"Зворотний польський запис (ЗПЗ): {' '.join(rpn)}")
        
        # 3. Обчислюємо результат
        result = calculate_rpn(rpn)
        print(f"Результат обчислення: {result}")
        
    except Exception as e:
        print(f"Помилка при обчисленні: {e}")